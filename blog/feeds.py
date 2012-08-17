#-*- coding: UTF-8 -*-

from django.contrib.syndication.feeds import Feed
from blog.models import Post

class LatestPosts(Feed):
    title=u'Xsank\'s Blog,生命不息，奋斗不止。。。。。。'
    linkUrl='http://xsank.net/'
    description=u'来自Xsank的更新'

    def itemsName(self):
        return Post.objects.filter(isPublished=True).order_by('-pubTime')[:6]

    def itemsLink(self,item):
        return self.linkUrl+'post/'+str(item.pk)+'/'
