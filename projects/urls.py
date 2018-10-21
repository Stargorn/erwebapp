from django.urls import path

from . import views

app_name = 'projects'
urlpatterns = [
    path('ourwork/', views.ProjectListView.as_view(), name='ourwork'),
    path('ourwork/<int:pk>/', views.ProjectDetailView.as_view(), name='detail'),
]
