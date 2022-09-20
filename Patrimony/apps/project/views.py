from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, DetailView, DeleteView, ListView
from django.views.generic.edit import UpdateView
from apps.project.models import Project, Transition, Evaluation
from django.utils import timezone
from apps.project.forms import ProjectForm, EvaluationForm, TransitionForm
from apps.rol.models import Profile
from apps.resource.models import Resource
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class ProjectList(LoginRequiredMixin, ListView):
    login_url = '/home/'
    model = Project
    template_name = 'project/project/project_list.html'


#Crear proyecto
@login_required(login_url='/')
def create_project(request):
    user = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.responsible = request.user
            project.finish = False
            if project.start_up > project.start_end:
                form = ProjectForm()
                msg = 'Datos de tiempo incorrectos'
                return render(request, 'project/project/create_project.html', {'form': form, 'user': user, 'msg': msg})
            project.save()
            form.save_m2m()
            return redirect('my_project_list')
    else:
        form = ProjectForm()
    return render(request, 'project/project/create_project.html', {'form': form, 'user': user})


@login_required(login_url='/')
def my_project_list(request):
    user = Profile.objects.get(user=request.user)
    pro = Project.objects.filter(authors=user).order_by('name')#Todos los Proyectos donde el usuario autenticado pertenece
    project = pro.exclude(responsible=user).order_by('name')
    project_my = Project.objects.filter(responsible=user).order_by('name')
    count = project.count() + project_my.count()
    return render(request, 'project/project/my_list.html', {'project': project, 'user': user, 'project_my': project_my, 'count': count})


@login_required(login_url='/',)
def project_details(request, pk):
    pro = Project.objects.get(pk=pk)
    user = Profile.objects.get(user=request.user)
    return render(request, 'project/project/project_details.html', {'project': pro, 'user': user})


@login_required(login_url='/')
def transition_for_my(request):
    trans = Transition.objects.filter(user_receiver=request.user)
    user = Profile.objects.get(user=request.user)
    project = Project.objects.filter(authors=user).order_by('name')
    return render(request, 'project/project/project_list_transition.html', {'trans': trans, 'user': user, 'project': project})


class ProjectDelete(DeleteView, LoginRequiredMixin):
    model = Project
    template_name = 'project/project/project_confirm_delete.html'
    success_url = reverse_lazy('my_project_list')


class ProjectUpdate(UpdateView, LoginRequiredMixin):
    model = Project
    fields = '__all__'
    template_name = 'project/project/project_update_form.html'
    success_url = '/home'


@login_required(login_url='/')
def create_transition(request, pk):
    user = Profile.objects.get(user=request.user)
    project = Project.objects.get(pk=pk)
    if request.method == 'POST':
        form = TransitionForm(request.POST)
        if form.is_valid():
            transition = form.save(commit=False)
            transition.user_giver = Profile.objects.get(user=request.user)
            transition.project = Project.objects.get(pk=pk)
            transition.category_new = Profile.objects.get(user=request.user).category
            transition.save()
            form.save_m2m()
            return redirect('home')
    else:
        form = TransitionForm()
        print(Profile.objects.get(user=request.user).category)
    return render(request, 'project/project/create_transition.html', {'user': user, 'form': form, 'project': project})


class TransitionDelete(DeleteView, LoginRequiredMixin):
    model = Transition
    template_name = 'project/project/transition_confirm_delete.html'
    success_url = reverse_lazy('home')


def my_transition_list(request):
    user = Profile.objects.get(user=request.user)
    transition = Transition.objects.filter(user_giver=user)
    print(transition)
    return render(request, 'project/project/my_transition_list.html', {'transition': transition})


@login_required(login_url='/')
def create_evaluation(request, pk):
    user = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = EvaluationForm(request.POST)
        if form.is_valid():
            evaluation = form.save(commit=False)
            evaluation.resource = Project.objects.get(pk=pk).resource
            evaluation.project = Project.objects.get(pk=pk)
            evaluation.save()
            form.save_m2m()
            return redirect('my_project_list')
    else:
        form = EvaluationForm()
        user = Profile.objects.get(user=request.user)
        resource = Project.objects.get(pk=pk).resource
        project = Project.objects.get(pk=pk)
    return render(request, 'project/evaluation/create_evaluation.html',
                  {'user': user, 'form': form, 'resource': resource, 'project': project}
                  )


@login_required(login_url='/')
def list_evaluation(request, pk):
    user = Profile.objects.get(user=request.user)
    resource = None
    project = None
    evaluation = None
    try:
        resource = Resource.objects.get(pk=pk)
        project = Project.objects.get(resource=resource)
        evaluation = Evaluation.objects.filter(project=project).order_by('time_create')
    except ObjectDoesNotExist:
        print("Objeto no existente")
    if resource and project and evaluation:
        return render(request, 'project/evaluation/evaluation_list.html',
                      {'user': user, 'evaluation': evaluation, 'project': project}
                      )
    else:
        return redirect('not_found')


def not_found(request):
    return render(request, 'project/evaluation/not_found.html')


class EvaluationDelete(DeleteView):
    model = Evaluation
    template_name = 'project/evaluation/evaluation_confirm_delete.html'
    success_url = reverse_lazy('home')


class A(UpdateView, LoginRequiredMixin):
    model = Evaluation
    fields = '__all__'
    template_name = 'project/evaluation/evaluation_historical.html'
    success_url = reverse_lazy('home')


class EvaluationUpdate(UpdateView, LoginRequiredMixin):
    model = Evaluation
    fields = '__all__'
    template_name = 'project/evaluation/evaluation_natural.html'
    success_url = reverse_lazy('home')


def evaluation_rol(request):
    user = Profile.objects.get(user=request.user)
    if user.category == 1:
        return redirect('/project/evaluation_social')
    if user.category == 2:
        return redirect('/project/evaluation_natural')
    if user.category == 3:
        return redirect('/project/evaluation_natural')
    else:
        return redirect('/')

