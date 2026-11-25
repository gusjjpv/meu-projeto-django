from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse

def home(request):
    return JsonResponse({
        "message": "Ola Mundo!",
        "status": "ok"
    })
