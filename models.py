from django.db import models

# Create your models here.
from django.contrib.auth.models import User




class Election(models.Model):           #election type = National elections
    title = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    
    def __str__(self):
        return self.title

class Position(models.Model):         #candidate position being voted for
    election = models.ForeignKey(Election, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.election.title})"
    
class Candidate(models.Model):        #person voted for
    name = models.CharField(max_length=200)
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='candidates/images', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name
    
class Voter(models.Model):     #person voting
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    has_voted = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.user.username).username
   
class Vote(models.Model):   #defines / outlines the relationship between voter and candidate(who voted for whom)
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE)
    candidate =models.ForeignKey(Candidate, on_delete=models.CASCADE)
    date_voted = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.voter} voted for {self.candidate} on {self.date_voted}"

    
