from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from talent_reserves.coaches.models import Coach
from .serializers import CoachSerializer


class CoachViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing accounts.
    """
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer


@api_view()
def get_ok(request):
    '''
    Тестовый endpoint для SwaggerUI
    '''
    return Response({"message": "ok"})
