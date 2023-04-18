from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import *
from django.views.generic import ListView,DetailView
from django.views.generic.edit import DeleteView,UpdateView
from .models import *
from django.db.models import Q

# Create your views here.
class ProjectCreationView(CreateView):
    form_class =ProjectCreationForm
    model = Project
    template_name = 'project/create_project.html'
    success_url = '/user/managerpage/'
    
    
    def form_valid(self, form):
        return super().form_valid(form)
        

class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = 'project/create_project.html'
    success_url = '/user/managerpage/'
    
class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project/project_detail.html'
    context_object_name = 'project_detail'
   
    def get(self, request, *args, **kwargs):
        labels = []
        data = []
        project = Project.objects.all().values()
        project1 = Project.objects.all().values_list('title', flat=True)
        time = Project.objects.all().values_list('estimated_time', flat=True)
        for i in project1:
            labels.append(i)
        for i in time:
             data.append(i)
        team = ProjectTeam.objects.filter(Project_id=self.kwargs['pk'])
        module = ProjectModule.objects.filter(project_id=self.kwargs['pk'])
        return render(request, self.template_name, {'project_detail': self.get_object(), 'team': team, 'module': module, 'labels': labels, 'data': data})
    
class ProjectDeleteView(DeleteView):
    model = Project
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    
    success_url = '/project/list_project/'    


class Create_Project_team(CreateView):
    form_class =ProjectTeamCreationForm
    template_name = 'project/project_team_create.html'
    success_url = '/project/list_project_team'

class ProjectTeamListView(ListView):
    model = ProjectTeam
    template_name = 'project/project_team_list.html'
    context_object_name = 'project_team_list'
    
class ProjectTeamByProject(ListView):
    model = ProjectTeam
    template_name = 'project/project_team_list.html'
    context_object_name = 'list_project_team'
    
    def get_queryset(self):
        return super().get_queryset().filter(Project_id=self.kwargs['pk'])    


class CreateProjectModule(CreateView):
    model = ProjectModule
    form_class = CreateProjectModuleForm
    template_name = 'project/project_module_create.html'
    success_url = '/project/list_project_module/'

    def get(self, request , *args: str, **kwargs):
        # print(self.kwargs['pk'])
        return super().get(request, *args, **kwargs)


# class ProjectModuleListByProject(ListView):
#     model = ProjectModule
#     template_name = 'project/project_module_list.html'
#     context_object_name = 'project_module_list'

#     def get_queryset(self):
#         return super().get_queryset().filter(project_id=self.kwargs['pk'])
    

class ProjectModuleList(ListView):
    model = ProjectModule
    template_name = 'project/project_module_list.html'
    context_object_name = 'project_module_list'

    # def get_queryset(self):
    #     return super().get_queryset().filter(project_id=self.kwargs['pk'])
    

class ModulesUpdateView(UpdateView):
    model = ProjectModule
    form_class = CreateProjectModuleForm
    template_name = 'project/project_module_create.html'
    success_url = '/project/list_project_module/'


class ModulesDeleteView(DeleteView):
    model = ProjectModule

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    success_url = '/project/list_project_module/'


class ProjectModuleDetailView(DetailView):
    model = ProjectModule
    template_name = 'project/project_module_detail.html'
    context_object_name = 'project_module_detail'

    def get(self, request, *args, **kwargs):
        team = ProjectTeam.objects.filter(Project_id=self.kwargs['pk'])
        print(self.kwargs['pk'])
        module = ProjectModule.objects.filter(id=self.kwargs['pk']).values()
        #print(module)
        project_task = Project_Task.objects.filter(module_id=self.kwargs['pk']).values()
        print(project_task)
        return render(request, self.template_name, {'team': team, 'module': module,'project_task':project_task})

class CreateProjectTask(CreateView):
    model = Project_Task
    form_class = CreateTaskForm
    template_name = 'project/create_project_task.html'
    success_url = '/project/list_project_module/'


class TeamDeleteView(DeleteView):
    model = ProjectTeam
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    success_url = '/project/list_project_team/'


class ModuleDetailView(DetailView):
    model = Project
    template_name = 'project/project_detail.html'
    context_object_name = 'module_detail_project'

    def get(self, request, *args, **kwargs):
        team = ProjectTeam.objects.filter(Project_id=self.kwargs['pk'])
        module = ProjectModule.objects.filter(project_id=self.kwargs['pk'])
        return render(request, self.template_name, {'project_detail': self.get_object(), 'team': team, 'module': module})
 
        