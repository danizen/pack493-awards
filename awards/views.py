from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render


@login_required
def den_list_view(request):
    return render(request, 'awards/dens.html')


@login_required
def scout_list_view(request):
	return render(request, 'awards/scouts.html')


@login_required
def show_den_view(request):
    return render(request, 'awards/aden.html')


@login_required
def show_scout_view(request):
    return render(request, 'awards/ascout.html')

