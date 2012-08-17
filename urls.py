from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.conf import settings
from django.views.decorators.cache import cache_page

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MiniBlog.views.home', name='home'),
    # url(r'^MiniBlog/', include('MiniBlog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'',include('MiniBlog.blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/',include('tinymce.urls')),
    (r'^comments/',include('django.contrib.comments.urls')),
    (r'^captcha/',include('captcha.urls')),
    (r'^admin/filebrowser/',include('filebrowser.urls')),
    url(r'^static/(?P<path>.*)$','django.views.static.serve',{'documentRoot':settings.STATIC_ROOT},name='media'),
    url(r'^grappelli/',include('grappelli.urls')),
    url(r'^static/image/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root':settings.STATIC_PATH},name="static"),
)
