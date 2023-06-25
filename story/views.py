from django.shortcuts import render
from . import models
# Create your views here.

def story(request):
    story = models.Story.objects.all()
    return render(request, 'story/index.html', {'story': story})

def story_detail(request, pk):
    story = models.Story.objects.get(pk=pk)
    return render(request, 'story/story_detail.html', {'story': story})

def chapter_detail(request, pk):
    chapter = models.Chapter.objects.get(pk=pk)
    return render(request, 'story/chapter_detail.html', {'chapter': chapter})

def latest_stories(request):
    stories = models.Story.objects.filter(chapters__isnull=False).order_by('-chapters__created_at')
    stories = list(dict.fromkeys(stories))
    return render(request, 'story/latest_story.html', {'stories': stories})