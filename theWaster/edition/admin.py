from django.contrib import admin

from edition.models import Edition, Article, Comment


admin.site.register(Edition)
admin.site.register(Article)
admin.site.register(Comment)