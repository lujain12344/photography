from django.db import models

# Create your models here.
class blog (models.Model):
    title=models.CharField(max_length=250)
    text=models.TextField()
    date=models.DateTimeField()

    def __str__(self):
        return self.title
