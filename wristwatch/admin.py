from django.contrib import admin
from .models import Soatlar_rasmlari, Soatlar

class SoatRasmlariInline(admin.TabularInline):
    model = Soatlar_rasmlari
    extra = 1  # Nechta qo'shimcha bo'sh forma bo'lishini belgilaydi

class SoatlarAdmin(admin.ModelAdmin):
    list_display = ('nomi', 'narxi',)  # Ro'yxatda ko'rsatiladigan ustunlar
    inlines = [SoatRasmlariInline]

admin.site.register(Soatlar, SoatlarAdmin)
