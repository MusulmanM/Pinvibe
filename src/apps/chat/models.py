from django.db import models

# Create your models here.

class Chat_User(models.Model):

     user=models.ForeignKey("users.User",on_delete=models.CASCADE,null=True,blank=True)
     share_pin=models.ForeignKey('pin.Pin',on_delete=models.CASCADE,null=True,blank=True)
     message=models.TextField(max_length=50)
class New_message(models.Model):
     chat_user=models.ForeignKey(Chat_User,on_delete=models.CASCADE, null=True, blank=True)
     user=models.ForeignKey("users.User",on_delete=models.CASCADE,null=True,blank=True)

class Chat(models.Model):
    user=models.ForeignKey("users.User",on_delete=models.CASCADE,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at=models.DateTimeField(auto_now=True, null=True, blank=True)
    new_message=models.ForeignKey(New_message,on_delete=models.CASCADE,null=True,blank=True)
    chat_user=models.ForeignKey(Chat_User,on_delete=models.CASCADE,null=True,blank=True)
