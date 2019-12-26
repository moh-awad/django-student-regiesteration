from django.conf.urls import url
from .views import *
from . import views
from .views import search
app_name = 'project_app'

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    # url(r'regiest/$',views.RegiestView.as_view(),name='regiest'),
    # url(r'regiest/$',views.RegiestView.as_view(),name='regiest'),
    # url(r'search/$', views.search, name='search'),
    url(r'search/$', search,name='search'),
    # url(r'detail/$',payment,name='payment'),

    ]
