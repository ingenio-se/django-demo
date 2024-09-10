from django.db import models

# Create your models here.
class Car(models.Model):
    title = models.TextField(max_length=100)
    year = models.TextField(max_length=4,null=True)
    
    def __str__(self):
        return self.title + ' - ' + self.year