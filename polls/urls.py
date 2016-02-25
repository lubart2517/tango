from django.conf.urls import patterns, url, include
from polls import views

urlpatterns = patterns('',
		url(r'^$', views.polls, name='polls'),
		)
urlpatterns += patterns('',
    url(r'^i18n/', include('django.conf.urls.i18n')),
)