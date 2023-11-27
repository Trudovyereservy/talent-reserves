from django.contrib import admin

from .models import News, ContentNews


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_content', 'date_published')

    def short_content(self, obj):
        if len(obj.content) > 50:
            return obj.content[:50] + '...'
        else:
            return obj.content
    short_content.short_description = 'Short Content'


class ContentNewsAdmin(admin.ModelAdmin):
    list_display = (
        'get_news_title', 'title_photo', 'author_photo', 'date_photo'
        )

    def get_news_title(self, obj):
        return obj.news.title if obj.news else None

    get_news_title.short_description = 'News Title'


admin.site.register(News, NewsAdmin)
admin.site.register(ContentNews, ContentNewsAdmin)
