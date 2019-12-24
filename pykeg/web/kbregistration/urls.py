from django.conf.urls import include
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from pykeg.web.kbregistration.forms import PasswordResetForm
from pykeg.web.kbregistration import views

urlpatterns = [
    url(r'^register/?$',
        views.register,
        name='registration_register'),
    url(r'^password/change/$',
        auth_views.PasswordChangeView.as_view(),
        name='password_change'),
    url(r'^password/change/done/$',
        auth_views.PasswordChangeDoneView.as_view(),
        name='password_change_done'),
    url(r'^password/reset/$',
        auth_views.PasswordResetView.as_view(),
        kwargs={'password_reset_form': PasswordResetForm},
        name='password_reset'),
    url(r'^password/reset/done/$',
        auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done'),
    url(r'^password/reset/complete/$',
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete'),
    url(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'),
    url('', include('registration.auth_urls')),
]
