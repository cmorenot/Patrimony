from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required
from .forms import LoginForm
from django.contrib.auth.models import User, Group
from .forms import SignUpForm
from .models import Profile
from apps.project.models import Project, Transition
from django.views.generic import CreateView, DetailView, DeleteView, ListView

from django.forms import ModelForm, TextInput
from django.urls import reverse_lazy

from django.views.generic.edit import UpdateView


from .forms import ContactForm
from django.views.generic.edit import FormView


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.category = form.cleaned_data.get('category')
            user.profile.boss = False
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'rol/signup.html', {'form': form})

