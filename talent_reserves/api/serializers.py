from rest_framework import serializers

from coaches.models import Coach


class CoachSerializer(serializers.ModelSerializer):
    """
    Сериализатор дя вывода информации о тренерах.
    Выводятся все поля, за исключением birthday.
    """
    directions = serializers.StringRelatedField(many=True)

    class Meta:
        model = Coach
        fields = ['surname', 'name', 'patronymic',
                  'achievements', 'directions', 'photo']
