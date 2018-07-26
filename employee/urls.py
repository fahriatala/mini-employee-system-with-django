"""employee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from homepage import views as homepage_views
from worker import views as worker_views
from presence import views as presence_views

urlpatterns = [
    url(r'^select2/', include('django_select2.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', worker_views.profile),
    url(r'^login/', homepage_views.login_view),
    url(r'^logout/', homepage_views.logout_view),
    url(r'^presence_list/', presence_views.presence_list),
    url(r'^presence_list2/', presence_views.presence_list2),
    url(r'^permit_application/', presence_views.permit_application),
    url(r'^permit_list/', presence_views.permit_list),
    url(r'^delete/(?P<pk>.+)$', presence_views.delete),
    url(r'^edit_permit/(?P<pk>.+)$', presence_views.edit_permit),     
]
