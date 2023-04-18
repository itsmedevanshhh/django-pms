from django.db import models
from user.models import User


status_choice = (("COMPLETED", "COMPLETED"),
                 ("PENDING", "PENDING"),
                 ("CANCELLED", "CANCELLED"))


class Status(models.Model):
    status_name = models.CharField(choices=status_choice, max_length=100)
    

    class Meta:
        db_table = 'status'

    def __str__(self):
        return self.status_name

# Create your models here.


status_choice = (("COMPLETED", "COMPLETED"),
                 ("PENDING", "PENDING"),
                 ("CANCELLED", "CANCELLED"))
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=100)
    estimated_time = models.IntegerField()
    start_date = models.DateField()
    completion_date = models.DateField()
    status = models.CharField(choices=status_choice, max_length=100,  null=True, blank=False)
    
    
    class Meta:
        db_table = 'project'
    
    def __str__(self):
        return self.title                    
        
   

class ProjectTeam(models.Model):

    Project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=False)
    user = models.ForeignKey( User, on_delete=models.CASCADE, null=True, blank=False)
    
    
    
    class Meta:
        db_table = 'project_team'


status_choice = (("COMPLETED", "COMPLETED"),
                 ("PENDING", "PENDING"),
                 ("CANCELLED", "CANCELLED"))
class ProjectModule(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    moduleName = models.CharField(max_length=100)
    description = models.TextField()
    estimeted_hours = models.IntegerField()
    status = models.CharField(choices=status_choice,max_length=100)
    startDate = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'project_module'

    def __str__(self):
        return self.moduleName


# Project Task Class
status_choice = (("Completed", "Completed"),
                 ("Pending", "Pending"),
                 ("Cancelled", "Cancelled"))
priorityChoice = (
    ('High', 'High Priority'),
    ('Less', 'Less Priority')
)


class Project_Task(models.Model):
   module = models.ForeignKey(ProjectModule, on_delete=models.CASCADE)
   project = models.ForeignKey(Project, on_delete=models.CASCADE)
   task_title = models.CharField(max_length=100)
   task_description = models.TextField()
   priority = models.CharField(choices=priorityChoice, max_length=30)
   user = models.ForeignKey( User, on_delete=models.CASCADE, null=True, blank=True)
   task_estimated_hours = models.IntegerField()
#    task_util_minutes = models.IntegerField()
   status = models.CharField(choices=status_choice, max_length=100)

   class Meta:
       db_table = 'project_task'

   def __str__(self):
       return self.task_title
   

badgeChoice = (
    ('InProgress', 'InProgress'),
    ('QuickFinisher', 'QuickFinisher'),
    ('LazyLoader', 'LazyLoader'),
    ('SilentUser', 'SilentUser')
)


class Badge(models.Model):
   badge = models.CharField(choices=badgeChoice, max_length=25)

   class Meta:
       db_table = 'badge'

   def __str__(self):
       return self.badge


# Project Team Class
status_choice = (("Completed", "Completed"),
                 ("Pending", "Pending"),
                 ("Cancelled", "Cancelled"))
badgeChoice = (
    ('IN', 'InProgress'),
    ('QF', 'QuickFinisher'),
    ('LL', 'LazyLoader'),
    ('SU', 'SilentUser')
)


class Project_Team_Module(models.Model):
    team_name = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(choices=status_choice, max_length=100)
    badge = models.CharField(choices=badgeChoice, max_length=25)

    class Meta:
        db_table = 'project_team_module'

    def __str__(self):
        return self.team_name
