from django.contrib import admin
from .models import OyoqKiyimlar, OyoqKiyimRasmlari

class OyoqKiyimlarRasmlariInline(admin.TabularInline):
    model = OyoqKiyimRasmlari
    extra = 1  # Nechta qo'shimcha bo'sh forma bo'lishini belgilaydi
    fields = ('rangi', 'rasmi',)  # Ko'rsatiladigan maydonlar

class OyoqKiyimlarAdmin(admin.ModelAdmin):
    list_display = ('nomi', 'narxi', 'olchamlari', 'zaxiradagi_soni')  # Ro'yxatda ko'rsatiladigan ustunlar
    inlines = [OyoqKiyimlarRasmlariInline]

admin.site.register(OyoqKiyimlar, OyoqKiyimlarAdmin)
