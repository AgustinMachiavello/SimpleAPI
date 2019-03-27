from django.urls import path, include
from .views import (
	CustomUserModelDetailAPIView,
	TaskModelDetailAPIView,
	TaskModelListAPIView,
	TaskModelCreateAPIView,
)
urlpatterns = [
	# Registration, login, logout url
	path('accounts/log/', include('rest_auth.urls')),
	path('accounts/register/', include('rest_auth.registration.urls')),

	path('users/get_by_id/<pk>/', CustomUserModelDetailAPIView.as_view(), name='user_detail_by_id'),
	path('tasks/get_by_id/<pk>/', TaskModelDetailAPIView.as_view(), name='task_detail_by_id'),
	path('tasks/list_all/', TaskModelListAPIView.as_view(), name='list_all_tasks'),
	path('tasks/create_new/', TaskModelCreateAPIView.as_view(), name='task_create_new'),
]