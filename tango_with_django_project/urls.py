from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from registration.backends.simple.views import RegistrationView
from solid_i18n.urls import solid_i18n_patterns
class MyRegistrationView(RegistrationView):
    def get_success_url(self,request, user):
        return '/rango/'

urlpatterns = solid_i18n_patterns('',
    # Examples:
    url(r'^$', 'tango_with_django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^rango/', include('rango.urls')),
	url(r'^polls/', include('polls.urls', namespace="polls")),
	#url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
	url(r'^accounts/', include('registration.backends.default.urls')),
)
urlpatterns += patterns('',
	url(r'^i18n/', include('django.conf.urls.i18n')),
)
if settings.DEBUG:
	urlpatterns += patterns(
	'django.views.static',
	(r'^media/(?P<path>.*)',
	'serve',
	{'document_root': settings.MEDIA_ROOT}), )