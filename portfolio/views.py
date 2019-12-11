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

def project_info(request,slug):

	#determine if slug was valid

	context = {
		'project_info': slug
	}
	
	return render(request, 'portfolio/projectinfo.html', context)