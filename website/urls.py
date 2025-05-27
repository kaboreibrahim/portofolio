from django.views.generic import RedirectView
from django.urls import path
from website.views import *
from django.views.i18n import set_language
urlpatterns = [
    path('', RedirectView.as_view(url='accueil/', permanent=True)),
    path('accueil/', index, name='accueil'),
    path('cv/', cv, name='cv'),
    path(r'^set_language/$', set_language, name='set_language'),
]


handler404 = error.custom_page_not_found_view
handler500 = error.custom_server_error_view
handler403 = error.custom_permission_denied_view
handler400 = error.custom_bad_request_view
