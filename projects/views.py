from django.shortcuts import render
#from django.views import generic

#from . import models


#class ProjectIndex(generic.ListView):
#    queryset = models.Project


def ourwork(request):
    render(request, 'projects/ourwork.html')
