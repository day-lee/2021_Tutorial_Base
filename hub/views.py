from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import Tutorial, Curriculum, Profile
from .filters import TutorialFilter
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.views import PasswordChangeView, PasswordChangeForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .forms import GoalForm, PasswordEditForm
from .forms import EditProfileForm


# class HomeView(ListView):
#     model = Tutorial
#     template_name = 'home.html'

#tutorial list test, urls
def HomeView(request):
    tutorials = Tutorial.objects.all()
    # tutorial = tutorials.tutoriallist_set.all() parent child relationship case
    myFilter = TutorialFilter(request.GET, queryset=tutorials)
    tutorials = myFilter.qs

    return render(request, 'home.html', {'tutorials': tutorials, 'myFilter': myFilter})
#context name




#243, home.html
#< button class ="btn btn-secondary reset_btn" type="submit" > < a class ="reset_btn" href="{% url 'hub:tutorial_list'%}" > Reset < / a > < / button >
#Tutorial
# def TutorialsList(request):
#     tutorials = Tutorial.objects.all()
#     # tutorial = tutorials.tutoriallist_set.all() parent child relationship case
#     myFilter = TutorialFilter(request.GET, queryset=tutorials)
#     tutorials = myFilter.qs
#     return render(request, 'tutorial_list.html', {'tutorials': tutorials, 'myFilter':myFilter})

from django.contrib.auth.mixins import LoginRequiredMixin
class TutorialDetailsView(DetailView):
    model = Tutorial
    template_name = 'tutorial_detail.html'
#object

#Users
class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('hub:home')

    def get_object(self):
        return self.request.user

class PasswordEditView(PasswordChangeView):
    form_class = PasswordEditForm
    success_url = reverse_lazy('hub:home')



#Curriculum
@login_required
def add_to_curriculum(request, pk):

    #if someone clicks my curriculum when there is no curriculum,(not added any tutorial) then redirects to home.
    #consider this.

    tutorial = get_object_or_404(Tutorial, pk=pk)
    Curriculum.objects.get_or_create(user=request.user)

    #어차피 하나면 그냥 curriculum = Curriculum.objects.filter(user= )[0]면 될것 같은데?
    curriculum_queryset = Curriculum.objects.filter(user=request.user)
    curriculum = curriculum_queryset[0]

    curriculum.tutorial.add(tutorial)
    messages.info(request, "Tutorial added to your curriculum")

    return redirect("hub:curriculum-summary")


@login_required
def remove_from_curriculum(request, pk):
    tutorial = get_object_or_404(Tutorial, pk=pk)
    curriculum = Curriculum.objects.filter(
                                            user=request.user,
                                            )[0]
    curriculum.tutorial.remove(tutorial)
    messages.info(request, "Tutorial removed from your curriculum")
    return redirect("hub:curriculum-summary")


@login_required
def CurriculumSummaryView(request):

    # curriculum count
    # curriculum_count = firstCustomer.curriculum_set.get().count()
    # return render(request, 'base.html', {'curriculum_count': curriculum_count})
    #


    try:
        curriculum = Curriculum.objects.get(user=request.user)
        #curriculum = Curriculum.objects.filter(user=request.user) #multiple curriculums...
        # context = {'curriculum': curriculum}

        tutorials = curriculum.tutorial.all()

        #tutorials = tutorials.tutoriallist_set.all() parent child relationship case
        myFilter = TutorialFilter(request.GET, queryset=tutorials)
        tutorials = myFilter.qs

        curriculum_count = tutorials.count()

        profile = Profile.objects.get(user=request.user)
        context = {'curriculum': curriculum, 'tutorials': tutorials, 'myFilter': myFilter,
                   'curriculum_count': curriculum_count, 'profile': profile}
        return render(request, 'curriculum_summary.html', context )

        # return render(request, 'curriculum_summary.html', context)

    except ObjectDoesNotExist:
        messages.error(request, "You do not have a curriculum, start by adding your first tutorial")
        return redirect("/") # CHANGE:  to tutorial list


#6 {% if request.user == curriculum.user %}
@login_required()
def UpdateGoalView(request, pk):
    goal = Profile.objects.get(id=pk)
    user_goal = Profile.objects.get(user=request.user)
    form = GoalForm(instance=goal)
    curriculum = Curriculum.objects.filter(user=request.user)
    context = {'goal': goal, 'form': form, 'curriculum': curriculum, 'user_goal':user_goal}
    #return render(request, 'update_goal.html', context)

    if request.method == 'POST':
        form = GoalForm(request.POST, instance=goal)
        if form.is_valid():
            form.save()
            return redirect('hub:curriculum-summary')
    return render(request, 'update_goal.html', context)

#<a href="{% url 'hub:update-goal' pk %}">Update</a>
# https://stackoverflow.com/questions/49592361/reverse-for-update-with-arguments-not-found-1-patterns-tried-veh



# def update_task(request, pk):
#     task = Task.objects.get(id=pk)
#     form = TaskForm(instance=task)
#     context = {'form': form}
#
#     return render(request, 'tasks/update_task.html', context)





class ContactView(ListView):
    model = Tutorial
    template_name = 'contact.html'

# TEST

class ProductView(DetailView):
    model = Tutorial
    template_name = 'product.html'

#home.html line20  <button type="button" class="btn btn-dark btn-lg download-button"> Register for Free</button>