from django.db import models

# Create your models here.
class UserInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    username=models.CharField('username',max_length=50,null=False,unique=True)
    password_hash=models.TextField('password',null=False)
    time_stamp = models.DateTimeField(auto_now_add=True)
    
    # creating a Meta class to tell django that do not overwrite this table it is already created
    class Meta:
        managed = True
        
        
        

    