from django.conf.urls import url

from . import views

app_name = 'film'
urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name = 'index'),
    url(r'^result/$', views.result, name = 'result'),
	url(r'^(?P<title>.+)/$', views.detail, name = 'detail'),
]
