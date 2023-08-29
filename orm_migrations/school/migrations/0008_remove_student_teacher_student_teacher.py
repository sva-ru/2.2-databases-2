# Generated by Django 4.2.4 on 2023-08-24 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0007_remove_student_teacher_student_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='teacher',
        ),
        migrations.AddField(
            model_name='student',
            name='teacher',
            field=models.ManyToManyField(related_name='teachers', to='school.teacher'),
        ),
    ]
