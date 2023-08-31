from django.http import HttpResponse
from rest_framework.decorators import api_view

@api_view(['GET'])
def hello_world(request):
    return HttpResponse("Hello World!")