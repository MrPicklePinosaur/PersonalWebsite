from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='portfolio-home'),
    path('projects/', views.projects, name='portfolio-projects'),
    path('projects/<slug:slug>/', views.project_info),
    path('about/', views.about, name='portfolio-about'),
]