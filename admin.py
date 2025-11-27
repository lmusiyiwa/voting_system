from django.contrib import admin
from .models import Voter, Vote, Election, Candidate, Position


# Register your models here.
admin.site.register(Voter)
admin.site.register(Vote)
admin.site.register(Election)
admin.site.register(Candidate)
admin.site.register(Position)
