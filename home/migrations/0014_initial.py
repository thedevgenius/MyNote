# Generated by Django 5.0.1 on 2024-02-09 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0013_remove_note_notebook_delete_target_delete_note_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, editable=False, max_length=300, null=True, unique=True)),
            ],
        ),
    ]
