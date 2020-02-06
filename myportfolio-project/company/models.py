from django.db import models

# Create your models here.

class company(models.Model):

    title=models.CharField(max_length=100)
    company=models.CharField(max_length=150)
    duration=models.CharField(max_length=100)
    summary=models.TextField()
    image=models.ImageField(upload_to='images/')
    salary = models.CharField(max_length=12,default=120)

    def __str__(self):
        return self.company
