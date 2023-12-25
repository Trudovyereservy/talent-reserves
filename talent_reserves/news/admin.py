from django.contrib import admin

from .models import ContentNews, News, TagNews, CommonTag


class ContentNewsInline(admin.TabularInline):
    model = ContentNews
    extra = 1


class TagNewsInline(admin.TabularInline):
    model = TagNews
    extra = 1


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description', 'date_published',
                    'created_at', 'updated_at')
    inlines = [ContentNewsInline, TagNewsInline]

    def short_description(self, obj):
        if len(obj.description) > 50:
            return obj.description[:50] + '...'
        else:
            return obj.description
    short_description.short_description = 'Short Description'


class ContentNewsAdmin(admin.ModelAdmin):
    list_display = (
        'get_news_title', 'image', 'title_photo', 'author_photo', 'date_photo',
        'created_at', 'updated_at')

    def get_news_title(self, obj):
        return obj.news.title if obj.news else None

    get_news_title.short_description = 'News Title'


class CommonTagAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug',)
    list_filter = ('name',)
    empty_value_display = '-empty-'


class TagNewsAdmin(admin.ModelAdmin):
    list_display = ('tag',)


admin.site.register(News, NewsAdmin)
admin.site.register(ContentNews, ContentNewsAdmin)
admin.site.register(TagNews, TagNewsAdmin)
admin.site.register(CommonTag, CommonTagAdmin)
