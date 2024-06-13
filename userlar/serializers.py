from rest_framework import serializers
from .models import User, Message, MessageToAdmin

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'telegram_user_id']

class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ['id', 'user', 'text', 'sent_at']

class MessageToAdminSerializer(serializers.ModelSerializer):

    class Meta:
        model = MessageToAdmin
        fields = ['id', 'user', 'text', 'sent_at']
