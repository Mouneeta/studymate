from django.db import models

# Create your models here.

class studyMat(models.Model):
    subject=models.CharField(max_length=100,default='SOME STRING')
    video=models.CharField(max_length=200)
    pdf=models.FileField(default="")
    def __str__(self):
        return self.subject
