from django.urls import path
from apps.rol import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
]
