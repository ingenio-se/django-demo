from django.db import models

# Create your models here.
class Car(models.Model):
    title = models.TextField(max_length=100)
    year = models.TextField(max_length=4,null=True)
    
    def __str__(self):
        return self.title + ' - ' + self.year
    
class Publisher(models.Model):
    name = models.TextField(max_length=100)
    address = models.TextField(max_length=100)
    def __str__(self):
        return self.name

class Author(models.Model):
    first_name = models.TextField(max_length=100)
    last_name = models.TextField(max_length=100)
    email = models.EmailField(max_length=100)
    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Book(models.Model):
    title = models.TextField(max_length=100)
    author = models.TextField(max_length=100)
    publication_date = models.DateField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author,related_name='authors')
    def __str__(self):
        return self.title
    
