# Generated by Django 5.0.1 on 2024-01-05 09:56

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_delete_note'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('category', models.CharField(choices=[('P', 'Prelims'), ('M', 'Mains')], max_length=1)),
                ('slug', models.SlugField(blank=True, editable=False, max_length=300, null=True, unique=True)),
                ('content', ckeditor.fields.RichTextField()),
                ('resources', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('notebook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.notebook', verbose_name='note_book')),
            ],
        ),
    ]