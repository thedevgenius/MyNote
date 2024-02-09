from django import template
from home.models import *

register = template.Library()

@register.filter
def get_count(value):
    subject = Subject.objects.get(id=value)
    count = Chapter.objects.filter(subject_id=subject.id).count()
    return count

