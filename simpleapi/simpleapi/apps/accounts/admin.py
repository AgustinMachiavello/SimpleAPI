from django.contrib import admin
from .models import CustomUser, Task

# Models registration
admin.site.register(CustomUser)
admin.site.register(Task)
