from django.db import models

# Create your models here.
"""
class Student:
    id=0
    name=''
    age=0
    email=''
"""

class Article(models.Model):
    id=models.IntegerField(primary_key=True)
    title=models.TextField(max_length=200)
    body=models.TextField(max_length=300)
    
    def __str__(self):
        return self.title



