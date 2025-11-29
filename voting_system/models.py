from django.db import models

class Leader(models.Model):
    name = models.CharField(max_length=1000)
    position = models.CharField(max_length=1000)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name
