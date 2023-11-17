from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def get_ok(request):
    '''
    Тестовый endpoint для SwaggerUI
    '''
    return Response({"message": "ok"})
