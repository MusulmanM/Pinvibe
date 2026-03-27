from django.db import models

# Create your models here.

class Save_Category(models.Model):
    name = models.CharField(max_length=200)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Pins (models.Model):
     pin = models.ForeignKey("pin.Pin",on_delete=models.CASCADE,null=True,blank=True )
     created_at = models.DateTimeField(auto_now_add=True)
     def __str__(self):
        return self.pin


class Board(models.Model):
    pin = models.ForeignKey("pin.Pin",on_delete=models.CASCADE,null=True,blank=True )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pin

class Callegue(models.Model):
    pin = models.ForeignKey("pin.Pin",on_delete=models.CASCADE,null=True,blank=True )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pin
    


class Save(models.Model):
    pin = models.ForeignKey("pin.Pin",on_delete=models.CASCADE,null=True,blank=True)
    user = models.ForeignKey("users.User",on_delete=models.CASCADE,null=True,blank=True)
    save_category = models.ForeignKey(Save_Category,on_delete=models.CASCADE,null=True,blank=True)
    pins = models.ForeignKey(Pins,on_delete=models.CASCADE,null=True,blank=True)
    boards = models.ForeignKey(Board,on_delete=models.CASCADE,null=True,blank=True)
    collages = models.ForeignKey(Callegue,on_delete=models.CASCADE,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pin) if self.pin else f"Save #{self.id or ''}"





class Create(models.Model):
    pins = models.ForeignKey(Pins,on_delete=models.CASCADE,null=True,blank=True)
    boards = models.ForeignKey(Board,on_delete=models.CASCADE,null=True,blank=True)
    collages = models.ForeignKey(Callegue,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        if self.pins:
            return str(self.pins)
        if self.boards:
            return str(self.boards)
        if self.collages:
            return str(self.collages)
        return f"Create #{self.id or ''}"