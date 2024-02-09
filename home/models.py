from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.
class Subject(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=300, blank=True, null=True, editable=False, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Chapter(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=300, blank=True, null=True, editable=False, unique=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, default='')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    


class Question(models.Model):
    title = models.CharField(max_length=1000)
    slug = models.SlugField(max_length=300, blank=True, null=True, editable=False, unique=True)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    answer = RichTextField()


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

