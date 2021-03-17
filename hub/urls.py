from django.urls import path
from . import views
from .views import (HomeView,
					TutorialDetailsView,
					UserRegisterView,
					CurriculumSummaryView,
					ProductView,
					)

app_name = 'hub'

urlpatterns = [
	path('', views.HomeView, name='home'), #HomeView.as_view()
	# path('tutorial_list/', views.TutorialsList, name='tutorial_list'),
	path('tutorial_details/<int:pk>', TutorialDetailsView.as_view(), name='tutorial_detail'),
	path('register/', UserRegisterView.as_view(), name='register'),
	path('add-to-curriculum/<pk>/', views.add_to_curriculum, name='add-to-curriculum'),
	path('remove-from-curriculum/<pk>/', views.remove_from_curriculum, name='remove-from-curriculum'),

	path('curriculum_summary/', CurriculumSummaryView, name='curriculum_summary'),

	path('product/<pk>/', ProductView.as_view(), name='product'),
]
