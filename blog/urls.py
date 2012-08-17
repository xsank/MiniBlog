#-*-coding:utf-8-*-

from django.conf.urls.defaults import *
from django.shortcuts import get_object_or_404
from django.views.decorators.cache import cache_page
from django.views.generic.simple import direct_to_template
from blog.models import *
from blog.views import *
from blog.feeds import *

feeds={'latest':LatestPosts,}

urlpatterns=patterns('',
    url(r'^$',postByPage,name='postByPage'),
    url(r'^search/$',search,name='postSearch'),
    url(r'^category/(？P<categoryID>\d+)/$',postByCategory,name='postByCategory'),
    url(r'^tag/(?P<tagID>\d+)/$',postByTag,name='postByTag'),
    url(r'^post/(?P<postID>\d+)/$',postByID,name='postByID'),
    url(r'^feeds/(?P<url>.*)/$','django.contrib.syndication.views.feed',{'feedDict':feeds}),
    url(r'^contact/$',contact),
    url(r'^contact/thanks/$',direct_to_template,{'template':'contact/ok.html'}),
    url(r'about/$',cache_page(direct_to_template,60*5),{'template':'about/about.html','extraContext':{'isAbout':u'关于网站'}}),
)
