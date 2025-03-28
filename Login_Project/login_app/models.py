from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    # name=models.CharField(max_length=20)
    age=models.IntegerField(null=True,blank=True,default=18)
    address=models.CharField(max_length=50)
    district=models.CharField(max_length=20)
    mobile=models.IntegerField(null=True,blank=True,default=18)
    # email=models.CharField(max_length=20)
    # username=models.CharField(max_length=20)
    # password=models.CharField(max_length=20)

    def __str__(self):
         return self.first_name
class Mark(models.Model):
     user_id=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
     semester_name=models.CharField(max_length=20)
     exam_mark=models.IntegerField()
     ce_mark=models.IntegerField()
     total_mark=models.IntegerField()
     grade=models.CharField(max_length=10)
     def __str__(self):
         return self.user_id.first_name