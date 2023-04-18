from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    
    path('create_project/',ProjectCreationView.as_view(),name='create_project'),
    path('create_project_task/', CreateProjectTask.as_view(), name='create_project_task'),
    path('project_module_detail/<int:pk>',ProjectModuleDetailView.as_view(),name='project_module_detail'),
    path('delete_project/<int:pk>',ProjectDeleteView.as_view(),name='delete_project'),
    path('update_project/<int:pk>',ProjectUpdateView.as_view(),name='update_project'),
    path('detail_project/<int:pk>',ProjectDetailView.as_view(),name='detail_project'),
    path('module_detail_project/<int:pk>',ModuleDetailView.as_view(),name='module_detail_project'),
    path('create_project_team/',Create_Project_team.as_view(),name='create_project_team'),
    path('list_project_team/',ProjectTeamListView.as_view(),name='project_team_list'),
    #path('list_project_team1/<int:pk>',ProjectTeamByProject.as_view(),name='project_team_list1'),
    path('create_project_module/', CreateProjectModule.as_view(),name='create_project_module'),
    #path('list_project_module/<int:pk>',ProjectModuleListByProject.as_view(), name='project_module_list'),
    path('list_project_module/',ProjectModuleList.as_view(), name='project_module_list'),
    path('modules_delete/<int:pk>',ModulesDeleteView.as_view(),name='modules_delete'),
    path('modules_update/<int:pk>',ModulesUpdateView.as_view(),name='modules_update'),
     path('delete_team/<int:pk>',TeamDeleteView.as_view(),name='delete_team'),
    
] 