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
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def HomeView(request):

#Filter
    context = {}
    filtered_tutorials            = TutorialFilter(
                                    request.GET,
                                    queryset=Tutorial.objects.all()
    )
    context['filtered_tutorials'] = filtered_tutorials

#Pagination
    paginated_filtered_tutorials  = Paginator(filtered_tutorials.qs, 8)
    page_number                   = request.GET.get('page')
    tutorial_page_obj             = paginated_filtered_tutorials.get_page(page_number)
    context['tutorial_page_obj']  = tutorial_page_obj

    return render(request, 'index.html', context=context)


class TutorialDetailsView(DetailView):
    model                         = Tutorial
    template_name                 = 'tutorial_detail.html'


#User
class UserRegisterView(generic.CreateView):
    form_class                    = UserCreationForm
    template_name                 = 'registration/register.html'
    success_url                   = reverse_lazy('login')


class UserEditView(generic.UpdateView):
    form_class                    = EditProfileForm
    template_name                 = 'registration/edit_profile.html'
    success_url                   = reverse_lazy('hub:home')

    def get_object(self):
        return self.request.user

    def get_context_data(self, **kwargs):
        context                   = super().get_context_data(**kwargs)
        context['profile']        = Profile.objects.all()
        return context

class PasswordEditView(PasswordChangeView):
    form_class                    = PasswordEditForm
    success_url                   = reverse_lazy('hub:home')


#Curriculum
@login_required
def add_to_curriculum(request, pk):
    tutorial                      = get_object_or_404(Tutorial, pk=pk)
    Curriculum.objects.get_or_create(user=request.user)
    curriculum_queryset           = Curriculum.objects.filter(user=request.user)
    curriculum                    = curriculum_queryset[0]
    curriculum.tutorial.add(tutorial)
    messages.info(request, "Tutorial added to your curriculum")
    return redirect("hub:curriculum-summary")

@login_required
def remove_from_curriculum(request, pk):
    tutorial                      = get_object_or_404(Tutorial, pk=pk)
    curriculum                    = Curriculum.objects.filter(
                                    user=request.user,
                                    )[0]
    curriculum.tutorial.remove(tutorial)
    messages.info(request, "Tutorial removed from your curriculum")
    return redirect("hub:curriculum-summary")

@login_required
def CurriculumSummaryView(request):
    try:
        context                     = {}
        curriculum                  = Curriculum.objects.get(user=request.user)
        tutorials                   = curriculum.tutorial.all()
        curriculum_count            = tutorials.count()
        context['curriculum_count'] = curriculum_count
        context['curriculum']       = curriculum
    #Filter

        filtered_tutorials          = TutorialFilter(
                                      request.GET,
                                      queryset=tutorials
        )
        context['filtered_tutorials'] = filtered_tutorials

    #Pagination
        paginated_filtered_tutorials = Paginator(filtered_tutorials.qs, 5)
        page_number                  = request.GET.get('page') #get the page
        tutorial_page_obj            = paginated_filtered_tutorials.get_page(page_number)
        context['tutorial_page_obj'] = tutorial_page_obj
        return render(request, 'curriculum_summary.html', context=context)

    except ObjectDoesNotExist:
        messages.info(request, "You do not have a curriculum yet, start by adding your first tutorial!")
        return redirect("hub:home")


@login_required()
def UpdateGoalView(request, pk):
    goal                             = Curriculum.objects.get(id=pk)  #user name?
    user_goal                        = Curriculum.objects.get(user=request.user)
    form                             = GoalForm(instance=user_goal)
    curriculum                       = Curriculum.objects.filter(user=request.user)
    context                          = {'goal': goal, 'form': form, 'curriculum': curriculum, 'user_goal':user_goal}


    if request.method == 'POST':
        form = GoalForm(request.POST, instance=goal)
        if form.is_valid():
            form.save()
            return redirect('hub:curriculum-summary')
    return render(request, 'update_goal.html', context)

class ContactView(ListView):
    model                            = Tutorial
    template_name                    = 'contact.html'


