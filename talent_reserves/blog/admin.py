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
    empty_value_display = '-пусто-'

    def get_tags(self):
        return ",".join([str(p) for p in self.tags.all()])


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'
