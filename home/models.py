from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.
class NoteBook(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=300, blank=True, null=True, editable=False, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    



    
class Note(models.Model):
    CAT_CHOICES = (
        ('P', "Prelims"),
        ('M', "Mains"),
    )
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=1, choices=CAT_CHOICES)
    notebook = models.ForeignKey(NoteBook, verbose_name="Note Book", on_delete=models.CASCADE)
    slug = models.SlugField(max_length=300, blank=True, null=True, editable=False, unique=True)
    content = RichTextField()
    resources = RichTextField(null=True, blank=True)

  
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    

class Target(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=255)
    status = models.BooleanField()
    
    def __str__(self):
        return f"{str(self.date)} - {self.title}"
