from django.conf.urls import include, url
from django.conf import settings
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required
from awards.views import (
    DensView, DenScoutsView, scout_list_view, 
    NewScoutView, UpdateScoutView, DeleteScoutView,
)
from accounts.views import login_view, profile_view, logout_view


def home(request):
    return HttpResponseRedirect(reverse('den-list'))


def about_view(request):
    return render(request, 'about.html')


def contact_view(request):
    return render(request, 'contact.html')


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^den/list/$', DensView.as_view(), name='den-list'),
    url(r'^den/(\d+)/scouts/$', DenScoutsView.as_view(), name='den-scouts'),
    url(r'^scout/list/$', scout_list_view, name='scout-list'),
    url(r'^scout/(\d+)/$', UpdateScoutView.as_view(), name='edit-scout'),
    url(r'^scout/$', NewScoutView.as_view(), name='new-scout'), 
    url(r'^scout/(\d+)/delete/$', DeleteScoutView.as_view(), name='delete-scout'), 
    url(r'^about/$', about_view, name='about'),
    url(r'^contact/$', contact_view, name='contact'),
    url(r'^accounts/profile/$', profile_view, name='profile'),
    url(r'^accounts/logout/$', logout_view, name='logout'),
    url(r'^accounts/login/$', login_view, name='login')
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns


