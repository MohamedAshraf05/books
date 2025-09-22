from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.title} - {self.id}"
