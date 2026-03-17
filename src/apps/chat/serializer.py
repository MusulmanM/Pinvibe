from rest_framework.serializers import ModelSerializer
from .models import Chat_User,Chat,New_message
class ChatSerializer(ModelSerializer):
    class Meta:
        model=Chat
        fields = "__all__"
class ChatUserSerializer(ModelSerializer):
    class Meta:
        model=Chat_User
        fields = "__all__"
class NewMessageSerializer(ModelSerializer):
    class Meta:
        model=New_message
        fields = "__all__"