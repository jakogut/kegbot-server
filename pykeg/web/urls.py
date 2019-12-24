# Copyright 2014 Bevbot LLC, All Rights Reserved
#
# This file is part of the Pykeg package of the Kegbot project.
# For more information on Pykeg or Kegbot, see http://kegbot.org/
#
# Pykeg is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# Pykeg is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Pykeg.  If not, see <http://www.gnu.org/licenses/>.


from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView
from django.urls import re_path

from pykeg.web.api import urls as api_urls
from pykeg.web.account import urls as account_urls
from pykeg.web.kbregistration import urls as registration_urls
from pykeg.web.kegadmin import urls as admin_urls
from pykeg.web.setup_wizard import urls as setup_urls
from pykeg.contrib.demomode import urls as demomode_urls
from pykeg.web.kegweb import urls as kegweb_urls

admin.autodiscover()

urlpatterns = [
    # api
    re_path(r'^api/(?:v1/)?', include(api_urls)),

    # kegbot account
    re_path(r'^account/', include(account_urls)),

    # auth account
    re_path(r'^accounts/', include(registration_urls)),

    # kegadmin
    re_path(r'^kegadmin/', include(admin_urls)),

    # Shortcuts
    re_path(r'^link/?$', RedirectView.as_view(pattern_name='kegadmin-link-device')),
]

if 'pykeg.web.setup_wizard' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^setup/', include(setup_urls)),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.KEGBOT_ENABLE_ADMIN:
    urlpatterns += [
        re_path(r'^admin/', admin.site.urls),
    ]

if settings.DEMO_MODE:
    urlpatterns += [
        re_path(r'^demo/', include(demomode_urls)),
    ]

# main kegweb urls
urlpatterns += [
    re_path(r'^', include(kegweb_urls)),
]
