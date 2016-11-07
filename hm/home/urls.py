from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^hostel/$', views.hostel, name='hostel'),
    url(r'^hostel/(?P<hostel_id>[-\w]+)/$', views.allhostel, name='allhostel'),
    url(r'^complaint/$', views.complaint, name='complaint'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.login, name='login'),
]