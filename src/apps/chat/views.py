from django.shortcuts import render
from .serializer import ChatSerializer,ChatUserSerializer,NewMessageSerializer
from .models import Chat_User,Chat,New_message
from rest_framework.viewsets import ModelViewSet
# Create your views here.
class ChatViewSet(ModelViewSet):
    queryset=Chat.objects.all()

    serializer_class=ChatSerializer
class ChatUserViewSet(ModelViewSet):
    queryset=Chat_User.objects.all()
    serializer_class=ChatUserSerializer
class NewMessageViewSet(ModelViewSet):
    queryset=New_message.objects.all()
    serializer_class=NewMessageSerializer