from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# views.py

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.shortcuts import render


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class CustomLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'registration/login.html'

class CustomLogoutView(LogoutView):
    next_page = '/'


class HomeView(TemplateView):
    template_name = 'landing.html'

class TodoListView(LoginView):
    success_url = 'todo_list/'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, self.template_name)
        else:
            return HttpResponse("User is not authenticated")
