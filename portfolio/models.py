# portfolio/models.py
from django.db import models

# Model for technology
class Technology(models.Model):
    name = models.CharField(max_length=100)
    badge = models.ImageField(upload_to='technologies/')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

# Featured Project Model
class FeaturedProject(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_completed = models.DateField()
    date_created = models.DateTimeField(auto_now_add=True)  # Saves the date when the project is created
    thumbnail = models.ImageField(upload_to='featured_projects/thumbnails/')
    slug = models.SlugField(unique=True)  # For URL reference
    technologies_used = models.ManyToManyField(Technology, related_name='featured_projects')

    def __str__(self):
        return self.title

# Quick Project Model
class QuickProject(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date_completed = models.DateField()
    date_created = models.DateTimeField(auto_now_add=True)  # Saves the date when the project is created
    thumbnail = models.ImageField(upload_to='quick_projects/thumbnails/')
    slug = models.SlugField(unique=True)  # For URL reference
    technologies_used = models.ManyToManyField(Technology, related_name='quick_projects')

    def __str__(self):
        return self.title

