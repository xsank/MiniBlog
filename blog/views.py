#-*-coding:utf-8-*-

from django.shortcuts import render_to_response,get_object_or_404,redirect
from django.views.generic import list_detail,date_based
from django.db.models import Q
from django import template
register=template.Library()
from django.http import HttpResponseRedirect
from blog.models import *
from blog.forms import *
from django.contrib.comments.models import *

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q=request.GET['q']
        queryset=Post.objects.filter(Q(title__icontains=q)|Q(body__icontains=q))
        if queryset:
            return list_detail.object_list(
                request,
                template_name='blog/post.html',
                template_object_name='post',
                queryset=queryset,
                extra_context={'isSearchResult':u'搜索结果'},
            )
        else:
            return render_to_response('search/badResult.html',{'isNoMatch':True,'isSearchResult':u'搜索结果'})
    else:
        return render_to_response('search/badResult.html',{'isSearchResult':u'搜索结果'})

def postByCategory(request,categoryID):
    category=get_object_or_404(Category,id=categoryID)
    queryset=category.post_set.filter(isPublished=True)
    return list_detail.object_list(
        template_object_name='post',
        template_name='blog/postList.html',
        queryset=queryset,
        paginate_by=10,
        extra_context={'isCategory':u'分类 '+category.cateName},
    )

def postByTag(request,tagID):
    tag=get_object_or_404(Tag,id=tagID)
    queryset=category.post_set.filter(isPublished=True)
    return list_detail.object_list(
        template_object_name='post',
        template_name='blog/postList.html',
        queryset=queryset,
        paginate_by=10,
        extra_context={'isTag':u'标签 '+tag.tagName},
    )

def postByPage(request):
    return list_detail.object_list(
        request,
        template_object_name='post',
        template_name='blog/postList.html',
        queryset=Post.objects.filter(isPublished=True),
        paginate_by=10,
    )

def postByID(request,postID):
    return list_detail.object_detail(
        request,
        template_object_name='post',
        template_name='blog/postList.html',
        object_id=postID,
        queryset=Post.objects.filter(isPublished=True),
    )

def contact(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            human=True
            cd=form.cleaned_data
            sendMail(
                cd['subject'],
                cd['message'],
                cd.get('email','test@qq.com'),
                ['test@qq.com'],
            )
            return HttpResponseRedirect('/contact/ok/')
    else:
        form=ContactForm()
    return  render_to_response('contact/contactme.html',{'form':form,'isContact':u'联系'})


