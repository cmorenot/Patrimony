from django.shortcuts import render, redirect, reverse
from apps.resource.forms import ResourceForm, GeoLocalizationForm, FixingActionsForm, AreaForm
from apps.resource.models import Resource, GeoLocalization, Area, FixingActions
from apps.rol.models import Profile
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.views.generic.edit import UpdateView
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime
from django.views.generic.detail import DetailView
from django.utils import timezone
from django.urls import reverse_lazy

from django.views.generic.edit import FormView


# Create your views here.


def create_resource(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST, request.FILES)
        if form.is_valid():
            resource = form.save(commit=False)
            if resource.reference_time.day > datetime.today().day or resource.reference_time.month > datetime.today().month or resource.reference_time.year > datetime.today().year:
                msg = 'Fecha debe ser menor que el dia de hoy'
                form = ResourceForm()
                return render(request, 'resource/create_resource.html', {'form': form, 'msg':msg})
            form.save()
            return redirect('list_resource')
    else:
        form = ResourceForm()
    return render(request, 'resource/create_resource.html', {'form': form})


class ResourceList(ListView):
    model = Resource


class ResourceDetailView(DetailView):
    model = Resource

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class ResourceUpdate(UpdateView):
    model = Resource
    fields = '__all__'
    template_name_suffix = '_update_form'


class ResourceDelete(DeleteView):
    model = Resource
    template_name = 'resource/resource_confirm_delete.html'
    success_url = reverse_lazy('list_resource')


def geo_localization_show(request, pk):
    resource = Resource.objects.get(pk=pk)
    try:
        geolocalization = GeoLocalization.objects.get(resource=resource)
    except ObjectDoesNotExist:
        print("El recurso solicitado, hasta ahora, no tiene localizacion geografica")
        return redirect('create_geolocalization', resource.pk)
    if geolocalization:
        return render(request, 'resource/geolocalization/show.html',
                      {'geolocalization': geolocalization, 'resource': resource})


def create_geolocalization(request, pk):
    user = Profile.objects.get(user=request.user)
    resource = Resource.objects.get(pk=pk)
    if request.method == 'POST':
        form = GeoLocalizationForm(request.POST)
        if form.is_valid():
            geloclization = form.save(commit=False)
            geloclization.resource = resource
            geloclization.save()
            form.save_m2m()
            print("salvado")
            return redirect('home')
    else:
        form = GeoLocalizationForm()
        resource = Resource.objects.get(pk=pk)
    return render(request, 'resource/geolocalization/create_geolocalization.html',
                  {'form': form, 'resource': resource, 'user': user}
                  )


def fixing_actions_show(request, pk):
    resource = Resource.objects.get(pk=pk)
    try:
        fixing_actions = FixingActions.objects.get(resource=resource)
    except ObjectDoesNotExist:
        print("El recurso solicitado, hasta ahora, no tiene accion correctiva")
        return redirect('fixing_actions_create', resource.pk)
    if fixing_actions:
        return render(request, 'resource/fixingActions/fixing_actions_show.html',
                      {'fixing_actions': fixing_actions, 'resource': resource})


def fixing_actions_create(request, pk):
    resource = Resource.objects.get(pk=pk)
    user = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = FixingActionsForm(request.POST, request.FILES)
        if form.is_valid():
            action = form.save(commit=False)
            action.user = user
            action.resource = resource
            form.save()
            form.save_m2m()
            return redirect('home')
    else:
        form = FixingActionsForm()
    return render(request, 'resource/fixingActions/fixing_actions_create.html', {'form': form})


def create_area(request):
    if request.method == 'POST':
        form = AreaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AreaForm()
    return render(request, 'resource/area/create_area.html', {'form': form})



