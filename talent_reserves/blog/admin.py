from django.contrib import admin

from .models import ContentPost, Post, Tag, TagPost


class ContentPostInline(admin.TabularInline):
    model = ContentPost
    extra = 1


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk',
                    'text',
                    'short_description',
                    'publication_date',
                    'get_tags',)
    list_filter = ('publication_date',)
    empty_value_display = '-empty-'
    inlines = [ContentPostInline]

    def get_tags(self, obj):
        return ",".join([str(p) for p in obj.tags.all()])


class ContentPostAdmin(admin.ModelAdmin):
    list_display = ('image',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug',)
    list_filter = ('name',)
    empty_value_display = '-empty-'


class TagPostAdmin(admin.ModelAdmin):
    list_display = ('tag',)


admin.site.register(Post, PostAdmin)
admin.site.register(ContentPost, ContentPostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(TagPost, TagPostAdmin)
