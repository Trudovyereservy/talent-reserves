from rest_framework import serializers

from coaches.models import Coach


class CoachSerializer(serializers.ModelSerializer):
    directions = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = Coach
        fields = ['surname', 'name', 'patronymic',
                  'achievements', 'directions', 'photo']
