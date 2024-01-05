# Generated by Django 5.0.1 on 2024-01-05 09:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_note_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='notebook',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='home.notebook', verbose_name='note_book'),
        ),
    ]