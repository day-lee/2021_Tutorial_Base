from django.urls import path
from . import views

from .views import (
					TutorialDetailsView,
					UserRegisterView,
					UserEditView,
					CurriculumSummaryView,
					ContactView,
					PasswordEditView
					)

app_name = 'hub'

urlpatterns = [
			path('', views.HomeView, name='home'),
			path('tutorial_details/<int:pk>', TutorialDetailsView.as_view(), name='tutorial_detail'),
			path('register/', UserRegisterView.as_view(), name='register'),
			path('edit-profile/', UserEditView.as_view(), name='edit-profile'),
			# path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html')),
			path('change-password/', PasswordEditView.as_view(template_name='registration/change_password.html')),
			path('add-to-curriculum/<pk>/', views.add_to_curriculum, name='add-to-curriculum'),
			path('remove-from-curriculum/<pk>/', views.remove_from_curriculum, name='remove-from-curriculum'),
			path('curriculum-summary/', CurriculumSummaryView, name='curriculum-summary'),
			path('edit/goal/<int:pk>', views.UpdateGoalView, name='update-goal'),
			path('contact/', ContactView.as_view(), name='contact'),

]
