from django.contrib import admin
from .models import Taqinchoqlar, Taqinchoqlar_rasmlari

class TaqinchoqlarRasmlariInline(admin.TabularInline):
    model = Taqinchoqlar_rasmlari
    extra = 1  # Nechta qo'shimcha bo'sh forma bo'lishini belgilaydi

class TaqinchoqlarAdmin(admin.ModelAdmin):
    list_display = ('nomi', 'narxi',)  # Ro'yxatda ko'rsatiladigan ustunlar
    inlines = [TaqinchoqlarRasmlariInline]

admin.site.register(Taqinchoqlar, TaqinchoqlarAdmin)
