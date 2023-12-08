from django.contrib import admin

from .models import ContentPost, Post, Tag, TagPost


class ContentPostInline(admin.TabularInline):
    model = ContentPost
    extra = 1


class TagPostInline(admin.TabularInline):
    model = TagPost
    extra = 1


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk',
                    'text',
                    'short_description',
                    'publication_date',
                    )
    list_filter = ('publication_date',)
    empty_value_display = '-empty-'
    inlines = [ContentPostInline, TagPostInline]


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
