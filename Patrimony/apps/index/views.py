from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from apps.rol.models import Profile, User
from apps.project.models import Transition
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


def login_view(request):
    msg = ''
    if not request.user:
        return HttpResponseRedirect('index/index')
    else:
        if request.POST:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('home/')
            else:
                msg = 'Usuario y/o password incorrecto'
                return render(request, 'index/failed.html', {'msg': msg},)
        ctx = {'msg': msg}
        return render(request, 'index/index.html', ctx,)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required(login_url='/')
def home(request):
    transition = Transition.objects.filter(user_receiver=request.user)
    user = Profile.objects.get(user=request.user)
    return render(request, 'project/home.html', {'user': user, 'transition': transition})


class ProfileList(ListView):
    model = Profile
