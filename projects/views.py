#from django.shortcuts import render
from django.views import generic

from . import models


class ProjectIndex(generic.ListView):
    queryset = models.Project.objects.all()
    template_name = 'projects/ourwork.html'
    
    

class ProjectDetail(generic.DetailView):
    model = models.Project
    template_name = 'projects/project.html'
     
#def ourwork(request):
#    render(request, 'projects/ourwork.html')
