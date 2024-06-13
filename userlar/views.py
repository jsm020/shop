from rest_framework import viewsets
from .models import User, Message, MessageToAdmin,ChatGroup
from .serializers import UserSerializer, MessageSerializer, MessageToAdminSerializer
from django.shortcuts import render
import datetime

def index(request):
    users = User.objects.exclude(id=request.user.id)
    return render(request, "index.html", {'users':users})

def chat(request, telegram_user_id):
    users = User.objects.exclude(id=request.user.id)
    print(request.user.id)
    user2 = User.objects.get(telegram_user_id=telegram_user_id)

    chatgroup = ChatGroup.objects.filter(users=user2).first()

    if not chatgroup:
        chatgroup = ChatGroup.objects.create(name=f"chat_with_{user2.telegram_user_id}")
        chatgroup.users.add(user2)

    context = {"users":users, "user":user2, "chatgroup":chatgroup}
    return render(request, 'chat.html',context)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
import json

class ChatMessageAPIView(APIView):
    def post(self, request, room_name):
        try:
            data = json.loads(request.body)
            message = data.get('message')
            sender_id = data.get('sender_id')
            
            if not message or not sender_id:
                return Response({'detail': 'Message and sender_id are required.'}, status=status.HTTP_400_BAD_REQUEST)
            
        except json.JSONDecodeError:
            return Response({'detail': 'Invalid JSON.'}, status=status.HTTP_400_BAD_REQUEST)
        
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            room_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender_id': sender_id,
                'time': datetime.now().strftime("%h-%d %H:%M")
            }
        )
        return Response({'status': 'message sent'}, status=status.HTTP_200_OK)
