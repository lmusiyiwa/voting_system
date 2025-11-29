from django.db import models

class Leader(models.Model):
    name = models.CharField(max_length=100)
    party = models.CharField(max_length=100)
    biography = models.TextField(blank=True, null=True)
    community_contribution = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='leaders/', blank=True, null=True)
    website = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.name

