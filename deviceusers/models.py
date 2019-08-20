from django.db import models


# Create your models here.
class Device_user(models.Model):
    class Meta:
        ordering = ('user_id',)
    user_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30,default="Unknown")
    password = models.CharField(max_length=255,blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return  str(self.user_id) + '   ' +  self.name

