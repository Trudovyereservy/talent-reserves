from django.contrib import admin
from feedback.models import Feedback


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    """
    Админ-панель модели обратной связи
    """
    list_display = ('name', 'email', 'subject', 'message', 'created_at')
    list_display_links = ('email',)
