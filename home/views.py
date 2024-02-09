from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from datetime import datetime
# Create your views here.
def home_page(request):
    subjects = Subject.objects.all().order_by('title')

    data = {
        'subjects' : subjects
    }
    return render(request, 'index.html', data)



def subject_details(request, slug):
    subject = get_object_or_404(Subject, slug=slug)
    chapters = Chapter.objects.filter(subject_id=subject.id)

    data = {
        'subject' : subject,
        'chapters' : chapters
    }
    return render(request, 'subject-details.html', data)

def chapter_details(request, slug):
    chapter = get_object_or_404(Chapter, slug=slug)
    questions = Question.objects.filter(chapter_id=chapter.id)
    subject = chapter.subject

    data = {
        'chapter' : chapter,
        'questions' : questions,
        'subject' : subject
    }
    return render(request, 'chapter-details.html', data)