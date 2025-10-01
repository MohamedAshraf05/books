from django.db import models

# Create your models here.

# Table A -> Table B


class Author(models.Model):
    name = models.CharField(max_length=140)
    age = models.CharField(max_length=14)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} - {self.phone_number}"

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.OneToOneField(Author , on_delete=models.CASCADE)
    year = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.id}"
