from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    titles=models.CharField(max_length=100)
    pub_dates=models.DateTimeField()
    bodys=models.TextField()
    urls= models.TextField()
    images=models.ImageField(upload_to='images/')
    icons=models.ImageField(upload_to='images/')
    votes_totals=models.IntegerField(default=1)
    hunters=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.titles

    def pub_date_pretty(self):
        return self.pub_dates.strftime('%b %e %Y')

# class New(models.Model):
#     titles=models.CharField(max_length=100)
#     pub_dates=models.DateTimeField()
#     bodys=models.TextField()
#     urls= models.TextField()
#     images=models.ImageField(upload_to='images/')
#     icons=models.ImageField(upload_to='images/')
#     votes_totals=models.IntegerField(default=1)
#     hunters=models.ForeignKey(User,on_delete=models.CASCADE)
