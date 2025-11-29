from rest_framework import serializers
from .models import Leader

class LeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leader
        fields = ['id', 'name', 'party', 'biography', 'community_contribution', 'date_of_birth', 'website']  # remove 'votes' if not in model
