from django.urls import path

from . import views

app_name = 'basesite'
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('success/', views.successView, name='success'),
]
