
from django.urls import path
from apps.project.views import ProjectList, create_project, create_evaluation, my_project_list, \
    project_details, transition_for_my, ProjectDelete, create_transition, TransitionDelete, \
    my_transition_list, ProjectUpdate, list_evaluation, EvaluationUpdate, \
    EvaluationDelete, not_found, evaluation_rol


urlpatterns = [
    path('project_list/', ProjectList.as_view(), name='project_list'),
    path('project_create/', create_project, name='create_project'),
    path('project_delete/<int:pk>/', ProjectDelete.as_view(), name='project_delete'),
    path('project_update/<int:pk>/', ProjectUpdate.as_view(), name='project_update'),
    path('project_details/<int:pk>/', project_details, name='project_details'),
    path('my_project_list/', my_project_list, name='my_project_list'),

    path('create_transition/<int:pk>/', create_transition, name='create_transition'),
    path('delete_transition/<int:pk>/', TransitionDelete.as_view(), name='delete_transition'),
    path('my_transition_list/', my_transition_list, name='my_transition_list'),
    path('transition_for_my/', transition_for_my, name='transition_for_my'),

    path('create_evaluation/<int:pk>/', create_evaluation, name='create_evaluation'),
    path('list_evaluation/<int:pk>/', list_evaluation, name='evaluation_list'),
    path('evaluation_update/<int:pk>/', EvaluationUpdate.as_view(), name='evaluation_update'),
    path('evaluation_delete/<int:pk>/', EvaluationDelete.as_view(), name='evaluation_delete'),
    path('evaluation_not_found/', not_found, name='not_found'),
    path('a/', evaluation_rol, name='a'),

]
