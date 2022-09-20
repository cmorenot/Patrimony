from django.urls import path
from apps.rol import views
from apps.resource import models
from apps.webServices import views

urlpatterns = [
    path('resource_ws/', views.resource_ws, name='resource_ws'),

]
