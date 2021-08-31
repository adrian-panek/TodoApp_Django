from django.db import models

class Task(models.Model):
    description = models.CharField(max_length=100)
    is_done = models.BooleanField()
    date_created = models.DateField(auto_now=True)

    def __str__(self):
        return self.description