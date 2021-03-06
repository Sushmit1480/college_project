# Generated by Django 3.1 on 2020-09-26 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fine',
            name='name',
        ),
        migrations.AddField(
            model_name='fine',
            name='student_name',
            field=models.CharField(default='Robot', max_length=40),
        ),
        migrations.AlterField(
            model_name='fine',
            name='branch',
            field=models.CharField(choices=[('IT', 'IT'), ('CSE', 'CSE'), ('MECH', 'MECH'), ('PROD', 'PROD'), ('CHEM', 'CHEM'), ('CIVIL', 'CIVIL'), ('TEXT', 'TEXT'), ('EXTC', 'EXTC'), ('ELECT', 'ELECT'), ('INSTRU', 'INSTRU')], default='IT', max_length=6),
        ),
    ]
