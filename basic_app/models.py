from django.db import models

# Create your models here.
class TODO(models.Model):
    added_date = models.DateTimeField()
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text
