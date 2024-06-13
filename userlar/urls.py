from django.urls import path
from .views import index, chat, ChatMessageAPIView

urlpatterns = [
    path('api/chat/<str:room_name>/', ChatMessageAPIView.as_view(), name='chat_message_api'),
    path('chat/', index, name="index"),
    path('chat/<str:telegram_user_id>/', chat, name="chat")
]
