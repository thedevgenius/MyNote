from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from datetime import datetime
# Create your views here.
def home_page(request):
    notebooks = NoteBook.objects.all().order_by('title')
    targets = Target.objects.filter(date__day=datetime.now().day, date__month=datetime.now().month, date__year=datetime.now().year, status=False)
    backlogs = Target.objects.filter(status=False).exclude(date__day=datetime.now().day, date__month=datetime.now().month, date__year=datetime.now().year)
    
    data = {
        'notebooks' : notebooks,
        'targets' : targets,
        'backlogs' : backlogs
    }
    return render(request, 'index.html', data)



def note_book_details(request, slug):
    notebook = get_object_or_404(NoteBook, slug=slug)
    pre_notes = Note.objects.filter(category='P', notebook_id=notebook.id)
    main_notes = Note.objects.filter(category='M', notebook_id=notebook.id)


    data = {
        'notebook' : notebook,
        'pre_notes' : pre_notes,
        'main_notes' : main_notes
    }
    return render(request, 'notebook.html', data)

def note_details(request, sl, slug):
    note = get_object_or_404(Note, slug=sl)
    notebook = NoteBook.objects.get(slug=slug)

    data = {
        'note' : note
    }

    return render(request, 'notes.html', data)

def edit_note(request, slug):
    note = get_object_or_404(Note, slug=slug)
    if request.method == 'POST':
        content = request.POST['note_content']
        note.content = content
        note.save()



    data = {
        'note' : note
    }
    return render(request, 'edit-note.html', data)


def target_finished(request, id):
    target = Target.objects.get(id=id)
    target.status = True
    target.save()
    return redirect('home')


def payment_testing(request):
    Target.objects.create(
        date=datetime.now(),
        title='My Target',
        status=False
    )
    return render(request, 'pay.html')