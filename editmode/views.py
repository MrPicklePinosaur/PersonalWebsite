from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms
from django.contrib import messages

# Create your views here.
@login_required
def createproject(request):
	#TODO: MOVE THE LOGIN REDIRECT FROM THE ADMIN TO A DEDICATED FORM
	if request.method =='POST': # if a post request was recieved
		form = forms.NewProjectForm(request.POST, request.FILES)
		if form.is_valid(): #validate that the data we got was actually from the form
			name = form.cleaned_data.get('name')
			messages.success(request, f'{name} successfully created!') #display a msg
			return redirect('portfolio-projects')
	else:
		form = forms.NewProjectForm()


	return render(request, 'editmode/createproject.html', {'form':form})
