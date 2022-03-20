from django.db import models

# Create your models here.
class examMan(models.Model):
    subject=models.CharField(max_length=100,default='some string')
    question=models.FileField(default="")
    script=models.FileField(default="")
    def __str__(self):
        return self.subject
