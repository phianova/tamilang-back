from django.db import models

# Create your models here.
class Letter(models.Model):
    tamil = models.CharField(max_length=2, default="")
    phonetic = models.CharField(max_length=5, default="")
    description = models.TextField(default="No description")
    sound = models.TextField(default="/")
    type = models.CharField(max_length=10, default="None")
    def __str__(self):
        return self.tamil
    