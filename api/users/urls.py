# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from rest_framework.urlpatterns import format_suffix_patterns

from users import views

urlpatterns = [
    url(r'^token/$',
        login_required(views.TokenView.as_view()),
        name='token'),
    url(r'^login/$',
        auth_views.LoginView.as_view(template_name='users/login.html'),
        name='login'),
    url(r'^logout/$',
        auth_views.LogoutView.as_view(template_name='users/logout.html'),
        name='logout'),
    url(r'^password_change/$',
        auth_views.PasswordChangeView.as_view(template_name='users/password_change.html'),
        name='password_change'),
    url(r'^password_change/done/$',
        auth_views.PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'),
        name='password_change_done'),
    url(r'^password_reset/$',
        views.PasswordResetView.as_view(),
        name='password_reset'),
    url(r'^password_reset/done/$',
        auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='users/password_reset_confirm.html'),
        name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view(
        template_name='users/password_reset_complete.html'),
        name='password_reset_complete'),
    # registration
    url(r'^activate/complete/$',
        TemplateView.as_view(template_name='users/registration_activation_complete.html'),
        name='registration_activation_complete'),
    # The activation key can make use of any character from the
    # URL-safe base64 alphabet, plus the colon as a separator.
    url(r'^activate/(?P<activation_key>[-:\w]+)/$',
        views.ActivationView.as_view(),
        name='registration_activate'),
    url(r'^register/$',
        views.RegistrationView.as_view(),
        name='registration_register'),
    url(r'^register/complete/$',
        TemplateView.as_view(
            template_name='users/registration_complete.html'
        ),
        name='registration_complete'),
    url(r'^register/closed/$',
        TemplateView.as_view(
            template_name='users/registration_closed.html'
        ),
        name='registration_disallowed'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
