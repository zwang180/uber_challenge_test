from django.conf.urls import url

from . import views

app_name = 'film'
urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^list/$', views.fullList.as_view(), name = 'list'),
    url(r'^result/$', views.result, name = 'result'),
	url(r'^detail/(?P<title>.+)/$', views.detail, name = 'detail'),
]
