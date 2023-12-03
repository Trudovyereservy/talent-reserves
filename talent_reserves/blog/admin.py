from django.contrib import admin

from blog.models import Post, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk',
                    'text',
                    'short_description',
                    'publication_date',
                    'get_tags',
                    'image')
    list_filter = ('publication_date',)
    empty_value_display = '-empty-'

    def get_tags(self, obj):
        return ",".join([str(p) for p in obj.tags.all()])


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug',)
    list_filter = ('name',)
    empty_value_display = '-empty-'
