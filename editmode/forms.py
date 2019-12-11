from django import forms
from django.forms import ModelForm
from . import models

class NewProjectForm(ModelForm):
	class Meta:
		model = models.Project
		fields = ['name','slug','summary','description','images','files']
