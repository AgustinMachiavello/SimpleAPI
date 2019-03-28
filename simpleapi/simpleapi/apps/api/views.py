# api/views.py

from django.shortcuts import render
from ..accounts.models import CustomUser, Task
from ..accounts.serializers import (
	CustomUserModelDetailSerializer,
	TaskModelDetailSerializer,
	TaskModelListSerializer,
	TaskModelCreateSerializer,
	TaskModelDeleteSerializer,
)
from rest_framework.generics import (
	ListAPIView,
	RetrieveAPIView,
	CreateAPIView,
	DestroyAPIView,
)


class CustomUserModelDetailAPIView(RetrieveAPIView):
	queryset = CustomUser
	serializer_class = CustomUserModelDetailSerializer


class TaskModelListAPIView(ListAPIView):
	queryset = Task
	serializer_class = TaskModelListSerializer


class TaskModelDetailAPIView(RetrieveAPIView):
	queryset = Task
	serializer_class = TaskModelDetailSerializer


class TaskModelCreateAPIView(CreateAPIView):
	queryset = Task
	serializer_class = TaskModelCreateSerializer

	def perform_create(self, serializer: TaskModelCreateSerializer):
		serializer.save(author=self.request.user)

class TaskModelDeleteAPIView(DestroyAPIView):
	queryset = Task
	serializer_class = TaskModelDeleteSerializer

