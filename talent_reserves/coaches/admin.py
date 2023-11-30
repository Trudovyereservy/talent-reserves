from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from .models import Coach, Direction


class CoachAdmin(admin.ModelAdmin):
    '''
    Класс отображения информации о тренерах в панели администратора.
    Метод photopraphy отображает маленькую фотографию тренера
    размером 100х100.
    Метод direction возвращает перечисление направлений работы тренера
    в виде одной строки (иначе ошибка, так как связь many-to-many).

    Названия полей photopraphy и direction изменены относительно названий
    аналогичных полей в модели (photo и directions), т.к. иначе Django
    отображает их в первоначальном виде.
    '''
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
    
    list_display = ["photography", "surname", "name", "patronymic",
                    "direction", "achievements", "birthday"]
    list_display_links = ["surname",]
    list_filter = ["directions",]
    ordering = ["surname"]
    
    # изменение интерфейса many-to-many связи на более приятный
    filter_horizontal = ["directions",]


admin.site.register(Coach, CoachAdmin)
admin.site.register(Direction)
