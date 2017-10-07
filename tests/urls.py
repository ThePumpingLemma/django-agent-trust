from __future__ import absolute_import, division, print_function, unicode_literals

from django.conf.urls import url
import django.contrib.auth.views

from . import views


urlpatterns = [
    url(r'^login/$', django.contrib.auth.views.login),
    url(r'^logout/$', django.contrib.auth.views.logout),

    url(r'^restricted/$', views.RestrictedView.as_view()),
    url(r'^trust/$', views.TrustView.as_view()),
    url(r'^session/$', views.SessionView.as_view()),
    url(r'^revoke/$', views.RevokeView.as_view()),
    url(r'^revoke_others/$', views.RevokeOthersView.as_view()),
]