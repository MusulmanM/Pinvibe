from django.db import models

# Create your models here.



class User(models.Model):
    class Role(models.TextChoices):
        SUPER_ADMIN = 'super_admin', 'super_admin'
        ADMIN = 'admin', 'admin'
        USER = 'user', 'user'
    
    username = models.CharField(max_length=55, unique=True)
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    phone_number = models.CharField(max_length=20, unique=True)
    gmail = models.CharField(max_length=155, unique=True)
    password = models.CharField(max_length=155)   #<<<---sha256
    data_of_birth = models.DateField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.username
    


class Profile(models.Model):
    class Role_profile(models.TextChoices):
        BUSINESS_PROFILE = 'business_profile', 'business_profile'
        PRIVATE_PROFILE = 'private_profile', 'private_profile'

    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    save = models.ForeignKey('save.Save', on_delete=models.CASCADE, null=True, blank=True)
    create = models.ForeignKey('save.Create', on_delete=models.CASCADE, null=True, blank=True)
    pin = models.ForeignKey('pin.Pin', on_delete=models.CASCADE, null=True, blank=True)
    chat = models.ForeignKey('chat.Chat', on_delete=models.CASCADE,)
    describtion = models.TextField()
    image = models.ImageField(upload_to='avatar/', blank=True, null=True)
    big_image = models.ImageField(upload_to='background/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.user
