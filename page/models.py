from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=150)
    email=models.EmailField()
    subject=models.CharField(max_length=150)
    massage=models.TextField()

    def __str__(self):
        return self.subject
