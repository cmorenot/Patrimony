from django.forms import ModelForm, Textarea, CharField, TextInput, SelectMultiple, Select, BooleanField, ModelMultipleChoiceField, ModelChoiceField, ChoiceField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from apps.rol.models import CATEGORY
from apps.rol.models import Profile
from apps.project.models import Project, Evaluation, Transition
from apps.resource.models import Resource
from django.utils.translation import gettext_lazy as _


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

        labels = {
            'name': _('Nombre:'),
            'authors': _('Autor(es):'),
            'resource': _('Recurso:'),
        }
        empty_label = {
            'name': _('Nombre:'),
            'authors': _('Autor(es):'),
            'resource': _('Recurso:'),
        }

        help_texts = {
            'name': _('Escriba el nombre del trabajo'),
            'authors': _('Seleccione integrante(s) de su equipo de trabajo'),
            'resource': _('Seleccione el recurso objetivo de su trabajo o añadalo en caso de  no estar'),
        }
        label = {
            'authors': _('--------'),
        }

        widgets = {
            'objective': Textarea(attrs={'rows': 2}),
            'authors': SelectMultiple(attrs={
                'class': 'mdb-select'
            }),
            'resource': Select(attrs={
                'class': 'mdb-select'
            }),
            'start_end': TextInput(
                attrs={'placeholder': 'Seleccione una fecha', 'class': 'form-control datepicker picker__input', 'readonly': 'readonly',
                       'aria-haspopup': 'true', 'aria-expanded': 'false', 'aria-readonly': 'false',
                       'aria-owns': 'date-picker-example_root'}),
            'start_up': TextInput(
                attrs={'placeholder': 'Seleccione una fecha', 'class': 'form-control datepicker picker__input', 'readonly': 'readonly',
                       'aria-haspopup': 'true', 'aria-expanded': 'false', 'aria-readonly': 'false',
                       'aria-owns': 'date-picker-example_root'}),

        }
        exclude = ['finish', 'responsible']


class EvaluationForm(ModelForm):
    class Meta:
        model = Evaluation
        fields = '__all__'

        widgets = {
            'reference_time': TextInput(
                attrs={'placeholder': 'Seleccione una fecha', 'class': 'form-control datepicker picker__input',
                       'readonly': 'readonly',
                       'aria-haspopup': 'true', 'aria-expanded': 'false', 'aria-readonly': 'false',
                       'aria-owns': 'date-picker-example_root'}),
            'qualitative_evaluation': Textarea(attrs={'rows': 2}),

        }

        exclude = ['resource', 'project']


class TransitionForm(ModelForm):
    class Meta:
        model = Transition
        fields = '__all__'
        exclude = ['user_giver', 'project', 'category_new', 'destroy']

        widgets = {
            'user_receiver': Select(attrs={
                'class': 'mdb-select'
            }),
            'time_is_over': TextInput(
                attrs={'placeholder': 'Seleccione una fecha', 'class': 'form-control datepicker picker__input',
                       'readonly': 'readonly',
                       'aria-haspopup': 'true', 'aria-expanded': 'false', 'aria-readonly': 'false',
                       'aria-owns': 'date-picker-example_root'}),
        }
