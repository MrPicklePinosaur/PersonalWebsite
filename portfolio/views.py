from django.shortcuts import render
from django.http import HttpResponse

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

def home(request):

	return render(request, 'portfolio/home.html')

def projects(request):
	context = {
		'projects': projects
	}

	print(context)

	return render(request, 'portfolio/projects.html', context)
