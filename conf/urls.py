from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from awards.views import den_list_view, den_scouts_view, den_awards_view
#from accounts.views import login_view, profile_view, logout_view, register_view, activate_view


def home(request):
    return HttpResponseRedirect(reverse('den-list'))


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^den/list/?$', den_list_view, name='den-list'),
    url(r'^den/([^/]+)/scouts/?$', den_scouts_view, name='den-scouts'),
    #url(r'^den/([^/]+)/scouts/([0-9]+)/?$', den_scout_view, name='den-scout'),
    url(r'^den/([^/]+)/awards/?$', den_awards_view, name='den-awards'),
    #url(r'^account/signin/?$', login_view, name='signin'),
    #ull(r'^account/profile/?$', profile_view, name='profile'),
    #url(r'^account/signout/?$', logout_view, name='signout'),
    #url(r'^account/register/?$', register_view, name='signup'),
    #url(r'^account/activate/?$', activate_view, name='activate'),
]

