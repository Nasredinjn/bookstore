from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import *


# Create your views here.

class SignUpView(CreateView):
    model = get_user_model()
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
