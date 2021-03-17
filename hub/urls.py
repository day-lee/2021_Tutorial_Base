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
	path('add-to-cart/<pk>/', views.add_to_cart, name='add-to-cart'),
	path('curriculum_summary/', CurriculumSummaryView, name='curriculum_summary'),

	path('product/<pk>/', ProductView.as_view(), name='product'),
]
