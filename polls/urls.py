from django.conf.urls import patterns, url, include
from polls import views

urlpatterns = patterns('',
		url(r'^$', views.IndexView.as_view(), name='index'),
	    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
        # ex: /polls/5/results/
        url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
        # ex: /polls/5/vote/
        url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
		)
urlpatterns += patterns('',
    url(r'^i18n/', include('django.conf.urls.i18n')),
)