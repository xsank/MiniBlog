#-*- coding: UTF-8 -*-

from django import template
register=template.Library()
from blog.models import *
from django.contrib.comments.models import *

@register.inclusion_tag('sidebar/category.html')
def blogCategory():
    return {'categories':Category.objects.all(),}

@register.inclusion_tag('sidebar/tag.html')
def blogTag():
    return {'tags':Tag.objects.all(),}

@register.inclusion_tag('sidebar/link.html')
def blogLink():
    return {'links':Link.objects.all(),}

@register.inclusion_tag('sidebar/recentComment.html')
def recentComment():
    return {'recentComment':Comment.objects.filter(is_public=True).order_by('-submit_date')[:10],}

@register.inclusion_tag('sidebar/recentPost.html')
def recentPost():
    return {'recentPost':Post.objects.filter(isPublished=True).order_by('-pubTime')[:6],}
