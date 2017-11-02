from django.contrib import admin

from edition.models import Edition, Article, Comment, Sort


class EditionModelAdmin(admin.ModelAdmin):
    list_display = ['edition', 'sort']
 
    class Meta:
        model = Edition

admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Edition, EditionModelAdmin)
admin.site.register(Sort)