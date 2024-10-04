from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Custom_User_Model(AbstractUser):
    User_type=[('viewer','Viewer'),('admin','Admin')]

    user_type=models.CharField(max_length=10,null=True,choices=User_type)



