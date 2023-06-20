from django.shortcuts import render
from . import models
# Create your views here.

def story(request):
    story = models.Story.objects.all()
    return render(request, 'story/index.html', {'story': story})

def story_detail(request, pk):
    story = models.Story.objects.get(pk=pk)
    return render(request, 'story/story_detail.html', {'story': story})