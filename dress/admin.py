from django.contrib import admin
from .models import AyollarKoylagi, AyollarKoylagiRasmlari

class AyollarKoylagiRasmlariInline(admin.TabularInline):
    model = AyollarKoylagiRasmlari
    extra = 1  # Nechta qo'shimcha bo'sh forma bo'lishini belgilaydi
    fields = ('rangi', 'rasmi',)  # Ko'rsatiladigan maydonlar

class AyollarKoylagiAdmin(admin.ModelAdmin):
    list_display = ('nomi', 'narxi', 'olchamlari', 'zaxiradagi_soni')  # Ro'yxatda ko'rsatiladigan ustunlar
    inlines = [AyollarKoylagiRasmlariInline]

admin.site.register(AyollarKoylagi, AyollarKoylagiAdmin)
