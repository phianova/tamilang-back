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
    
class UserLearning(models.Model):
    STATUS_CHOICES = (
        ('not_known', 'Not Known'),
        ('learning', 'Learning'),
        ('learned', 'Learned'),
    )

    username = models.CharField(max_length=10, default="")
    learning_status = models.JSONField(default=dict)  # Stores letter status as {"letter_id": "status"}

    def set_status(self, letter_id, status):
        self.learning_status[str(letter_id)] = status
        self.save()

    def get_status(self, letter_id):
        return self.learning_status.get(str(letter_id), 'not_known')

    def __str__(self):
        return self.username
