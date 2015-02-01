from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from urlshortener_app import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'urlshortener.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index),
    url(r'^(?P<short_url>[a-z0-9]+)/?$', views.redirect_short_url),
    url(r'^admin/', include(admin.site.urls)),
)
