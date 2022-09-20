from django.urls import path
from .views import login_view, logout_view, home, ProfileList


urlpatterns = [
    path('', login_view, name='index'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('home/', home, name='home'),


    path('profile/', ProfileList.as_view()),
]
