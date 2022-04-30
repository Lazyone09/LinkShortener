from rest_framework.decorators import api_view
from rest_framework.response import responses
from rest_framework.views import APIView
from django.http import JsonResponse


@api_view(['GET'])
def use_api_view(request):
    foo = bool(request.GET['isgay'])
    if foo is True:
        return JsonResponse({'Moisey': 'Moisey pidor'})
    else:
        return JsonResponse({'Moisey': 'Moisey NE pidor'})
