# Generated by Django 5.0.1 on 2024-01-05 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_note_resources'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='category',
            field=models.CharField(choices=[('P', 'Prelims'), ('M', 'Mains')], max_length=1),
        ),
    ]
