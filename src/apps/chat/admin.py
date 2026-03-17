from django.contrib import admin
from .models import New_message,Chat_User,Chat
# Register your models here.
admin.site.register(New_message)
admin.site.register(Chat_User)
admin.site.register(Chat)