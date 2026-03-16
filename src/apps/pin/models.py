from django.db import models

# Create your models here.

class Pin_category(models.Model):
    name = models.CharField(max_length=155)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Pin(models.Model):
    pin_category = models.ForeignKey(Pin_category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='pin/')
    name = models.CharField(max_length=155)
    description = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.pin_category}"