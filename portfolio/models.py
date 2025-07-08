# portfolio/models.py
from django.db import models
from django.utils.text import slugify

# Model for technology
class Technology(models.Model):
    name = models.CharField(max_length=100)
    badge = models.ImageField(upload_to='technologies/')
    description = models.TextField(blank=True)

    class Meta:
        verbose_name ="Technology"
        verbose_name_plural ="Technologies"

    def __str__(self):
        return self.name





# Featured Project Model
class FeaturedProject(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    repository_link = models.URLField(blank=True)
    date_completed = models.DateField(blank=True, null=True)
    date_created = models.DateField(auto_now_add=True)  # Saves the date when the project is created
    thumbnail = models.ImageField(upload_to='featured_projects/thumbnails/')
    slug = models.SlugField(unique=True)  # For URL reference
    technologies_used = models.ManyToManyField(Technology, related_name='featured_projects')

    class Meta:
        verbose_name ="Featured Project"
        verbose_name_plural ="Featured Projects"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


# Screenshot Model for Multiple Images
class Screenshot(models.Model):
    project = models.ForeignKey(FeaturedProject, related_name='screenshots', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='projects/screenshots/')
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Screenshot for {self.project.title}"


# Quick Project Model
class QuickProject(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date_completed = models.DateField()
    date_created = models.DateTimeField(auto_now_add=True)  # Saves the date when the project is created
    repository_link = models.URLField(blank=True)
    thumbnail = models.ImageField(upload_to='quick_projects/thumbnails/')
    slug = models.SlugField(unique=True)  # For URL reference
    technologies_used = models.ManyToManyField(Technology, related_name='quick_projects')

    class Meta:
        verbose_name ="Quick Project"
        verbose_name_plural ="Quick Projects"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

