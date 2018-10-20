from django.urls import path

from . import views

app_name = 'projects'
urlpatterns = [
    path('ourwork/', views.ProjectIndex.as_view(), name='ourwork'),
    path('ourwork/<int:pk>/', views.ProjectDetail.as_view(), name='detail'),
]
