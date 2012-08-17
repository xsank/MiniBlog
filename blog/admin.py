#-*-coding:utf-8-*-

from django.contrib import admin
from blog.models import *

class PostAdmin(admin.ModelAdmin):
    filter_horizontal = ('categories','tags')
    list_display = ('title','isPublished','pubTime','id')
    date_hierarchy = 'pubTime'

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author=request.user
        obj.save()

class LinkAdmin(admin.ModelAdmin):
    list_display = ('linkName','linkUrl','id')

admin.site.register(Link,LinkAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post,PostAdmin)
admin.site.register(Message)


