from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.models import Count

from .models import Candidate, Voter, Vote, Election

# Create your views here.

def home(request):
    """Landing/home page - list all candidates for voting"""
    candidates = Candidate.objects.all()
    return render(request, 'candidate_list.html', {'candidates': candidates})

def cast_vote(request):
    """Handle vote casting - process POST request from candidate_list.html"""
    if request.method == 'POST':
        candidate_id = request.POST.get('candidate_id')
        
        if not candidate_id:
            return render(request, 'candidate_list.html', {
                'candidates': Candidate.objects.all(),
                'error': 'Please select a candidate.'
            })
        
        try:
            candidate = Candidate.objects.get(id=candidate_id)
        except Candidate.DoesNotExist:
            return render(request, 'candidate_list.html', {
                'candidates': Candidate.objects.all(),
                'error': 'Candidate not found.'
            })
        
        # Get or create a default anonymous user for voting
        user, _ = User.objects.get_or_create(username='anonymous_voter')
        voter, _ = Voter.objects.get_or_create(user=user)
        
        # Check if voter already voted
        if voter.has_voted:
            return render(request, 'already_voted.html', {'voter_name': 'Anonymous Voter'})
        
        # Record the vote
        Vote.objects.create(voter=voter, candidate=candidate)
        voter.has_voted = True
        voter.save()
        
        return redirect('results')
    
    # GET request - show voting form
    candidates = Candidate.objects.all()
    return render(request, 'candidate_list.html', {'candidates': candidates})

def results(request):
    """Display election results with vote counts"""
    # Annotate candidates with vote counts
    candidates_with_votes = Candidate.objects.annotate(
        vote_count=Count('vote')
    ).order_by('-vote_count')
    
    total_votes = Vote.objects.count()
    
    return render(request, 'results.html', {
        'candidates': candidates_with_votes,
        'total_votes': total_votes
    })