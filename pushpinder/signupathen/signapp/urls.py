"""signupathen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views

urlpatterns = [


    # url(r'^$', views.index, name='index'),
    # url(r'^get/$', views.index, name='index'),
    # url(r'^details/(?P<id>\w)/$', views.details, name='details'),
    # url(r'^add/$', views.add, name='add'),
    # url(r'^delete/$', views.delete, name='delete'),
    # url(r'^update/$', views.update, name='update'),
    # url(r'^feedback/$', views.feedback, name='feedback'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^success/$', views.success, name='success'),
    url(r'^confirm/(?P<activation_key>\w+)/$', views.signup_confirm,name='signup_confirm'),
    # url(r'^password/$', views.change_password, name='change_password'),
    url(r'^login/$', views.login1, name='login'),
    url(r'^logout/$', views.logout1, name='logout'),
    # url(r'^delete_account/$', views.delete_account, name='delete_account'),

    # url(r'^chart/$', views.chart, name='chart'),
    # url(r'^ajax/data/$', views.ajax_data, name='ajax_data'),


]
