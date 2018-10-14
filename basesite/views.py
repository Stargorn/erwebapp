from django.shortcuts import render


def home(request):
    return render(request, 'basesite/home.html')

def about(request):
    return render(request, 'basesite/about.html')

def contact(request):
    return render(request, 'basesite/contact.html')
