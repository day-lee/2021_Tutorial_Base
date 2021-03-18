from django.urls import path
from . import views


from .views import (HomeView,
					TutorialDetailsView,
					UserRegisterView,
					UserEditView,
					CurriculumSummaryView,
					ProductView,
					ContactView,

					PasswordEditView
					)

app_name = 'hub'

urlpatterns = [
	path('', views.HomeView, name='home'), #HomeView.as_view()
	# path('tutorial_list/', views.TutorialsList, name='tutorial_list'),
	path('tutorial_details/<int:pk>', TutorialDetailsView.as_view(), name='tutorial_detail'),

	path('register/', UserRegisterView.as_view(), name='register'),
	path('edit-profile/', UserEditView.as_view(), name='edit-profile'),
	# path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html')),
	path('change-password/', PasswordEditView.as_view(template_name='registration/change_password.html')),

	path('add-to-curriculum/<pk>/', views.add_to_curriculum, name='add-to-curriculum'),
	path('remove-from-curriculum/<pk>/', views.remove_from_curriculum, name='remove-from-curriculum'),
	path('curriculum-summary/', CurriculumSummaryView, name='curriculum-summary'),

	path('product/<pk>/', ProductView.as_view(), name='product'),

	#path('add-goal', AddGoalView.as_view(), name="add-goal"),
	path('goal/edit/<int:pk>', views.UpdateGoalView, name='update-goal'),


	path('contact/', ContactView.as_view(), name='contact'),



]
