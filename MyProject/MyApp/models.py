from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Custom_User_Model(AbstractUser):
    User_type=[('viewer','Viewer'),('admin','Admin')]

    user_type=models.CharField(max_length=10,null=True,choices=User_type)
    Profile_Pic=models.ImageField(upload_to='Media/Profile_Pic',null=True)

class ViewerProfileModel(models.Model):

    user=models.ForeignKey(Custom_User_Model,on_delete=models.CASCADE,null=True,related_name='ViewerProfile')


class AdminProfileModel(models.Model):

    user=models.ForeignKey(Custom_User_Model,on_delete=models.CASCADE,null=True,related_name='AdminProfile')


    