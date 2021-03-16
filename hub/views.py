from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from .models import Tutorial, Curriculum
from .filters import TutorialFilter
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


class HomeView(ListView):
    model = Tutorial
    template_name = 'home.html'


def TutorialsList(request):
	tutorials = Tutorial.objects.all()
	# tutorial = tutorials.tutoriallist_set.all() parent child relationship case
	myFilter = TutorialFilter(request.GET, queryset=tutorials)
	tutorials = myFilter.qs
	return render(request, 'tutorial_list.html', {'tutorials': tutorials, 'myFilter':myFilter})
# tutorial_list, line 85,  <td><a href="{% url 'tutorial_detail' item.pk %}">{{item.title}}</a></td>


class TutorialDetailsView(DetailView):
    model = Tutorial
    template_name = 'tutorial_detail.html'


class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')