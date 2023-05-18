from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .views import *

CustomUser = get_user_model()


class CustomUserAdmin(ModelAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'username', 'is_superuser')
    search_fields = ('username',)
    fields = ["username","email","user_permissions","password"]

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Permission)
