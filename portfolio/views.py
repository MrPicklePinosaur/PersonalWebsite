from django.shortcuts import render
from django.http import HttpResponse



def home(request):

	return render(request, 'portfolio/home.html')

def about(request):

	return render(request, 'portfolio/about.html')

def projects(request):

	projects = [
		{
			'name': 'Shinobi Network',
			'link': 'github.pinosaur/shinobi-network',
			'description': 'multiplayer shooter created with libgdx'
		},
		{
			'name': 'Soulless',
			'link': 'github.pinosaur/soulless',
			'description': 'platformer created for ludum dare 45'
		}
	]

	context = {
		'projects': projects
	}

	return render(request, 'portfolio/projects.html', context)

