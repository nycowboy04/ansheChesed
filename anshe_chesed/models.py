from django.db import models

# Create your models here.
class CAC(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField()
    address1=models.CharField(max_length=100)
    address2=models.CharField(max_length=25, blank=True)
    city=models.CharField(max_length=25)
    state=models.CharField(max_length=15)
    zip=models.CharField(max_length=10)
    poomo=models.IntegerField(max_length=2)

class PoopMonster(models.Model):
    fam=models.ForeignKey(CAC)
    first_name=models.CharField(max_length=50)
    birthday=models.TextField()
