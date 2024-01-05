from django import template
from home.models import *

register = template.Library()

@register.filter
def get_count(value):
    notebook = NoteBook.objects.get(id=value)
    note_count = Note.objects.filter(notebook_id=notebook.id).count()
    return note_count

