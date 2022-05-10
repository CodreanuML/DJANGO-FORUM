from django.shortcuts import render,redirect
from .forms  import SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib import messages


# Create your views here.
def sign_up_view(request):


	if request.method=="POST":

		form=SignUpForm(request.POST)

		if form.is_valid():
			user_creation=form.save()
			messages.success(request, 'User created successfuly !')
			auth_login(request,user_creation)
			return redirect('TWEET:home')


		else:
			messages.warning(request, 'Try again ! Use a stronger password or another username !')
		
	else:


		form=SignUpForm()

	return render(request,'signup.html',{'form':form})