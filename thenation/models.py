from django.db import models

# Create your models here.
# for adding slides
    
class Contacts(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=300)
    subject=models.CharField(max_length=3000,default="")    
    query=models.CharField(max_length=50,default="")
    
    def __str__(self):
        return self.name

