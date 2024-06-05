from django.contrib import admin
from .models import boshqa_mahuslot, boshqa_mahuslot_rasmlari

class boshqa_mahuslotRasmlariInline(admin.TabularInline):
    model = boshqa_mahuslot_rasmlari
    extra = 1  # Nechta qo'shimcha bo'sh forma bo'lishini belgilaydi

class boshqa_mahuslotAdmin(admin.ModelAdmin):
    list_display = ('nomi', 'narxi',)  # Ro'yxatda ko'rsatiladigan ustunlar
    inlines = [boshqa_mahuslotRasmlariInline]

admin.site.register(boshqa_mahuslot, boshqa_mahuslotAdmin)
