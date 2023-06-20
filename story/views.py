from django.shortcuts import render
from . import models
# Create your views here.

def story(request):
    story = models.Story.objects.all()
    return render(request, 'story/index.html', {'story': story})