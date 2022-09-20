from django.forms import ModelForm, Textarea, CharField, TextInput, Select, FileField,BooleanField, ModelMultipleChoiceField, Form, ClearableFileInput, FloatField, IntegerField,ImageField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from apps.rol.models import CATEGORY
from apps.rol.models import Profile
from apps.project.models import Project
from apps.resource.models import Resource, GeoLocalization, FixingActions, Area
from django.utils.translation import gettext_lazy as _


class ResourceForm(ModelForm):
    class Meta:
        model = Resource
        fields = '__all__'

        labels = {
            'name': _('Nombre:'),
            'direction': _('Dirección')
        }
        empty_label = {
            'name': _('Nombre:'),
            'direction': _('Dirección')
        }

        help_texts = {
            'name': _('Escriba el nombre del trabajo'),
            'authors': _('Seleccione integrante(s) de su equipo de trabajo'),
            'resource': _('Seleccione el recurso objetivo de su trabajo o añadalo en caso de  no estar'),
        }

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control'
            }),
            'alternative_of_use': Textarea(attrs={'rows': 2}),
            'direction': Textarea(attrs={'rows': 2}),
            'description': Textarea(attrs={'rows': 2}),
            'other_values': Textarea(attrs={'rows': 2}),
            'existing_use': Textarea(attrs={'rows': 2}),

            'reference_time': TextInput(
                attrs={'placeholder': 'Seleccione una fecha', 'class': 'form-control datepicker picker__input',
                       'readonly': 'readonly',
                       'aria-haspopup': 'true', 'aria-expanded': 'false', 'aria-readonly': 'false',
                       'aria-owns': 'date-picker-example_root'}),
            'type': Select(attrs={
                'class': 'mdb-select'
            }),
            'protection_grade': Select(attrs={
                'class': 'mdb-select'
            }),

        }


class GeoLocalizationForm(ModelForm):
    class Meta:
        model = GeoLocalization
        fields = '__all__'
        exclude = ['resource']


class FixingActionsForm(ModelForm):
    class Meta:
        model = FixingActions
        fields = '__all__'
        exclude = ['user', 'resource']

        widgets = {
            'description': Textarea(attrs={'rows': 2}),
            'existing_use': Textarea(attrs={'rows': 2}),
            'time': TextInput(
                attrs={'placeholder': 'Seleccione una fecha', 'class': 'form-control datepicker picker__input',
                       'readonly': 'readonly',
                       'aria-haspopup': 'true', 'aria-expanded': 'false', 'aria-readonly': 'false',
                       'aria-owns': 'date-picker-example_root'}),

        }


class AreaForm(ModelForm):
    class Meta:
        model = Area
        fields = '__all__'
