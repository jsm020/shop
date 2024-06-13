from django.db import models
import requests

class User(models.Model):
    first_name = models.CharField(max_length=30)
    telegram_user_id = models.BigIntegerField(unique=True)

    def __str__(self):
        return f'{self.telegram_user_id}'

class ChatGroup(models.Model):
    name = models.CharField(max_length=250)
    users = models.ManyToManyField(User)
    def __str__(self):
        return str(self.name)

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.user}'



class MessageToAdmin(models.Model):
    user = models.ForeignKey(Message, on_delete=models.CASCADE)
    text = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.user     }'