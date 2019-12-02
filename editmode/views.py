from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
@login_required
def createproject(request):
	form = forms.NewProjectForm()
	return render(request, 'editmode/createproject.html',{'form':form})
