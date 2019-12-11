from django.shortcuts import render
from django.http import HttpResponse

from editmode.models import Project

def home(request):

	return render(request, 'portfolio/home.html')

def about(request):

	return render(request, 'portfolio/about.html')

def projects(request):

	context = {
		'projects': Project.objects.all()
	}

	return render(request, 'portfolio/projects.html', context)

def project_info(request,project_slug):

	#determine if slug was valid
	proj = Project.objects.filter(slug=project_slug).first()

	#TODO: check to see if its a valid slug (if the query that was returned is not NULL)

	context = {
		'info': proj #bad solution: make sure that the slug is unique later
	}

	return render(request, 'portfolio/projectinfo.html', context)