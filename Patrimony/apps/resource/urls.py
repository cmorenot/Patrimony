
from django.urls import path
from apps.resource.views import create_resource, ResourceList, ResourceDetailView, ResourceUpdate, ResourceDelete, \
    geo_localization_show, create_geolocalization, fixing_actions_create, create_area, fixing_actions_show

urlpatterns = [
    path('create_resource/', create_resource, name='create_resource'),
    path('detail_resource/<int:pk>/', ResourceDetailView.as_view(), name='resource_detail'),
    path('update_resource/<int:pk>/', ResourceUpdate.as_view(), name='resource_update'),
    path('delete_resource/<int:pk>/', ResourceDelete.as_view(), name='resource_delete'),
    path('list_resource', ResourceList.as_view(), name='list_resource'),

    path('geolocalization_show/<int:pk>/', geo_localization_show, name='geo_localization_show'),
    path('geolocalization_create/<int:pk>/', create_geolocalization, name='create_geolocalization'),

    path('fixing_actions_create/<int:pk>/', fixing_actions_create, name='fixing_actions_create'),
    path('fixing_actions_show/<int:pk>/', fixing_actions_show, name='fixing_actions_show'),


    path('create_area/', create_area, name='create_area'),
    #path('list_area/', list_area, name='list_area'),

]
