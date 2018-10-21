#from django.shortcuts import render
from django.views import generic

from . import models


class ProjectListView(generic.ListView):
    model = models.Project
    queryset = models.Project.objects.all()
    template_name = 'projects/ourwork.html'
    
    

class ProjectDetailView(generic.DetailView):
    model = models.Project
    template_name = 'projects/project.html'
     
#def ourwork(request):
#    render(request, 'projects/ourwork.html')
