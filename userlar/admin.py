from django.contrib import admin
from .models import Message,ChatGroup,User
# Register your models here.
@admin.register(User)  # User modelini admin panelida ro'yxatga olish
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'telegram_user_id')  # Ro'yxatda ko'rsatiladigan maydonlar
    search_fields = ('first_name', 'telegram_user_id')  # Qidiruv maydonlari
    list_filter = ('first_name',) 
admin.site.register(ChatGroup)
admin.site.register(Message)
