# accounts/serializers.py
from rest_framework import serializers
from .models import CustomUser, Task


class CustomUserModelDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = CustomUser
		fields = '__all__'


class TaskModelDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields = '__all__'


class TaskModelListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields = ('id', 'title', 'creation_date', 'author',)


class TaskModelCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields = ('title', )
