from django.db import models

class Blog(models.Model):
    title=models.CharField(max_length=100)
    pub_date=models.DateTimeField()
    blog_text=models.TextField(max_length=500)
    image=models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.blog_text[:200]

    def pub_date_smart(self):
        return self.pub_date.strftime('%b %e %Y')
