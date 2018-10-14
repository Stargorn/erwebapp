from django.shortcuts import render


def ourwork(request):
    render(request, 'projects/ourwork.html')
