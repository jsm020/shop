# main/views.py

from django.shortcuts import render
from django.http import HttpResponse

def page(request):
    user_location = request.META.get('REMOTE_ADDR', None)  # Foydalanuvchi manzilini olish
    return HttpResponse(f"Foydalanuvchi joylashuvi: {user_location}")
