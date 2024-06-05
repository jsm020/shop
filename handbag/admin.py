from django.contrib import admin
from .models import Sumkalar_rasmlari, Sumkalar

class SumkalarRasmlariInline(admin.TabularInline):
    model = Sumkalar_rasmlari
    extra = 1  # Nechta qo'shimcha bo'sh forma bo'lishini belgilaydi

class SumkalarAdmin(admin.ModelAdmin):
    list_display = ('nomi', 'narxi',)  # Ro'yxatda ko'rsatiladigan ustunlar
    inlines = [SumkalarRasmlariInline]

admin.site.register(Sumkalar, SumkalarAdmin)
