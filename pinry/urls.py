from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = patterns('',
                       url(r'', include('pinry.core.urls', namespace='core')),
                       url(r'', include('pinry.users.urls', namespace='users')),
)
urlpatterns += staticfiles_urlpatterns()
urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
