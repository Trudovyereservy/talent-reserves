from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from .models import Coach, Direction


class CoachAdmin(admin.ModelAdmin):
    list_display = ["photography", "surname", "name", "patronymic",
                    "direction", "achievements", "birthday"]
    ordering = ["surname"]

    def photography(self, obj):
        try:
            url = obj.photo.url
            return mark_safe(f'<img src={url} width="100" height="100">')
        except:
            return "No photo available"
       
    def	direction(self, obj):
        return ', '.join(
            [direction.title for direction in obj.directions.all()]
        )


admin.site.register(Coach, CoachAdmin)
admin.site.register(Direction)
