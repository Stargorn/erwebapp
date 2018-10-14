from django.urls import path

from . import views

app_name = 'projects'
urlpatterns = [
    path('ourwork/', views.ourwork, name='ourwork'),
]
