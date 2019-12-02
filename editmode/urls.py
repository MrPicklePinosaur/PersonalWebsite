from django.urls import path
from . import views

urlpatterns = [
    path('createproject/', views.createproject, name='editmode-createproject'),
]