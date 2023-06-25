from django.db import models
from taggit.managers import TaggableManager


# Create your models here.
class Story(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField("Category", related_name="stories")
    tag = TaggableManager()
    # TODO add author field

    def __str__(self):
        return self.title


class Chapter(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name="chapters")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Comment(models.Model):
    content = models.TextField()
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
