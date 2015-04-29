from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'shrtnr.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'app.views.index', name='index'),
    url(r'^(?P<linkid>[a-zA-Z0-9]+)$', 'app.views.view', name='view'),
]
