from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from awards.views import den_list_view, show_den_view, scout_list_view, show_scout_view
from accounts.views import login_view, profile_view, logout_view


def home(request):
    return HttpResponseRedirect(reverse('den-list'))


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^den/list/$', den_list_view, name='den-list'),
    url(r'^den/(\d+)/$', show_den_view, name='show-den'),
    url(r'^scout/list/$', scout_list_view, name='scout-list'),
    url(r'^scout/(\d+)/$', show_scout_view, name='show-scout'),
    url(r'^accounts/profile/$', profile_view, name='profile'),
    url(r'^accounts/logout/$', logout_view, name='logout'),
    url(r'^accounts/login/$', login_view, name='login')
]

