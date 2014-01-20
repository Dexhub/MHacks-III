from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mhack.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^login/$','mhack_web.views.login'),
	url(r'^friends/$','mhack_web.views.friends'),
	url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_DOC_ROOT}),
	url(r'^login2/$','mhack_web.views.login2'),	
	url(r'^login3/$','mhack_web.views.login3'),
	url(r'^postcards/$','mhack_web.views.postcard'),
	url(r'^mug/$','mhack_web.views.mug'),
	url(r'^order/$','mhack_web.views.order'),
	url(r'^poster/$','mhack_web.views.poster'),
	
)
