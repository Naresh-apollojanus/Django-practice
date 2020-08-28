from django.db import models


# Create your models here.
class CookInfo(models.Model):
    phone_no = models.CharField(max_length=20)
    pan_no = models.IntegerField()


class Cook(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    cook_info = models.OneToOneField(CookInfo, on_delete=models.PROTECT, null=True)
    profile_pic = models.ImageField(upload_to='cook', null=True)

    def __str__(self):
        return self.name


class Speciality(models.Model):
    name = models.CharField(max_length=20)
    cooks = models.ManyToManyField(Cook)


class FoodItem(models.Model):
    name = models.CharField(max_length=250, default=0)
    qty = models.IntegerField(default=0)
    price = models.FloatField()
    discount = models.FloatField(default=0)
    cook = models.ForeignKey(Cook, on_delete=models.PROTECT, null=True)
