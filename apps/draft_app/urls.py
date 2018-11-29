from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^user/(?P<id>\d+)$', views.Show),
    url(r'^user/(?P<id>\d+)/lineup$', views.My_Lineup),
    url(r'^user/(?P<id>\d+)/lineup/(?P<pos>[A-Z]+)$', views.Lineup_position),
    url(r'^user/(?P<id>\d+)/lineup/create$', views.Lineup_create),
    url(r'^user/(?P<id>\d+)/lineup/add/(?P<p_id>\d+)$', views.Add),
    url(r'^position/(?P<id>[A-Z]+)$', views.Position),
    url(r'^home$', views.Home),
    url(r'^team/(?P<id>\d+)$', views.Team_id),
    url(r'^new$', views.New),
    url(r'^register$', views.Register),
    url(r'^login$', views.Login),
    url(r'^logout$', views.Logout),
]