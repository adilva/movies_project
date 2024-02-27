from django.db import models

# Create your models here.
class Movie(models.Model):
    name=models.CharField(max_length=250)
    desc=models.TextField()
    year=models.IntegerField()
    img=models.ImageField(upload_to='pics')
    
    
    def _str_(self):
        return self.name