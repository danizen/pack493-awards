from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import (
	login as login_view,
	logout as logout_view,
)


@login_required
def profile_view(request):
	'''
	Show the profile and privileges of the user
	'''
	render(request, 'registration/profile.html')
