#-*-coding:utf-8-*-

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from MiniBlog.tinymce import models as tinymce_models

class Category(models.Model):
    cateName=models.CharField(max_length=50)

    def __unicode__(self):
        return self.cateName

class Tag(models.Model):
    tagName=models.CharField(max_length=50)

    def __unicode__(self):
        return self.tagName

class Post(models.Model):
    author=models.ForeignKey(User,related_name='posts')
    title=models.CharField(max_length=100)
    pubTime=models.DateTimeField('Date Published',auto_now_add=True)
    upTime=models.DateTimeField('Date Update',auto_now=True)
    categories=models.ManyToManyField(Category,blank=True,null=True)
    tags=models.ManyToManyField(Tag,blank=True,null=True)
    excerpt=tinymce_models.HTMLField()
    body=tinymce_models.HTMLField()
    isPublished=models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering=['-pubTime']

    def isBigestID(self):
        if self.id >= Post.objects.filter(isPublished=True).order_by('-id')[0].id:
            return True

    def isSmallestID(self):
        if self.id >=Post.objects.filter(isPublished=True).order_by('id')[0].id:
            return True

    def prevPostTitle(self):
        return Post.objects.get(id=self.id-1).title

    def nextPostTitle(self):
        return Post.objects.get(id=self.id+1).title

class Link(models.Model):
    linkName=models.CharField(max_length=50)
    linkUrl=models.URLField(max_length=150)

    def __unicode__(self):
        return self.linkName

class Message(models.Model):
    username=models.CharField(max_length=15)
    email=models.EmailField()
    message=models.TextField(max_length=200)
    subTime=models.DateTimeField(auto_now_add=True)
    ipAddress=models.IPAddressField(null=True)
    isPublic=models.BooleanField(default=True)
    isRemoved=models.BooleanField(default=False)

    def __unicode__(self):
        return u"%s发消息：%s" % (self.username,self.message[:50])

    class Meta:
        ordering=['-subTime']

    def save(self,*args,**kwargs):
        super(Message,self).save(*args,**kwargs)


