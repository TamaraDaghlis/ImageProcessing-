from django.db import models

# Create your models here.
class Car(models.Model):
    plateNumber = models.IntegerField(null= False, unique= True)
    carType = models.CharField(max_length=30 )

    def __str__(self):
        return self.plateNumber


class Image(models.Model):
    image = models.ImageField(upload_to= "images")