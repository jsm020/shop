from django.contrib import admin
from .models import Parfemeriya_rasmlari, Parfemeriya

class ParfemeriyaRasmlariInline(admin.TabularInline):
    model = Parfemeriya_rasmlari
    extra = 1  # Nechta qo'shimcha bo'sh forma bo'lishini belgilaydi

class PardfemeriyaAdmin(admin.ModelAdmin):
    list_display = ('nomi', 'narxi',)  # Ro'yxatda ko'rsatiladigan ustunlar
    inlines = [ParfemeriyaRasmlariInline]

admin.site.register(Parfemeriya, PardfemeriyaAdmin)
