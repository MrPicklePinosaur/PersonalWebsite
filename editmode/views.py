from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def createproject(request):
	#REDIRECT TO PROPER LOGIN PAGE!!!!!!
	return render(request, 'editmode/createproject.html')
