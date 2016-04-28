from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render


#@login_required
def den_list_view(request):
    return render(request, 'awards/dens.html')


#@login_required
def den_scouts_view(request):
    return render(request, 'awards/scouts.html')


#@login_required
def den_awards_view(request):
    return render(request, 'awards/awards.html')

