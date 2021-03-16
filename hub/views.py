from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from .models import Tutorial, Curriculum
from .filters import TutorialFilter

class HomeView(ListView):
    model = Tutorial
    template_name = 'home.html'


def TutorialsList(request):
	tutorials = Tutorial.objects.all()
	# tutorial = tutorials.tutoriallist_set.all() parent child relatioship case
	myFilter = TutorialFilter(request.GET, queryset=tutorials)
	tutorials = myFilter.qs
	return render(request, 'tutorial_list.html', {'tutorials': tutorials, 'myFilter':myFilter})