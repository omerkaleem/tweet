from django.conf.urls import patterns, include, url
from twitter import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'twitter.views.home', name='home'),
    # url(r'^twitter/', include('twitter.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
  (r'^$', views.login),
	(r'^login/$', views.login),
	(r'^validate_login/$', views.validate_login),
	(r'^submittweet/$', views.submittweet),
	(r'^make_new_account/$', views.make_new_account),
	
)
