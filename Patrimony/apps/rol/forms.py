from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from apps.rol.models import CATEGORY
from django.utils.translation import gettext_lazy as _
from django.forms import PasswordInput, ModelForm, Textarea, CharField, TextInput, SelectMultiple, Select, BooleanField, ModelMultipleChoiceField, ModelChoiceField, ChoiceField


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput(render_value=False))


"""class SignUpForm(UserCreationForm):
    birth_date = forms.ChoiceField(CATEGORY, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'birth_date', 'password1', 'password2', )


class ProjectForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(), help_text='Nombre del Proyecto')
"""


class SignUpForm(UserCreationForm):
    category = forms.ChoiceField(choices=CATEGORY, help_text='No requerido', label='Categoria')

    class Meta:
        model = User
        fields = ('username', 'category', 'password1', 'password2', 'email', 'first_name', 'last_name', 'is_active')
        exclude = ['boss']


class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass
