from django.conf import settings

if getattr(settings, 'LOGOUT_REDIRECT_URL', None) is None:
    setattr(settings, 'LOGOUT_REDIRECT_URL', '/')

