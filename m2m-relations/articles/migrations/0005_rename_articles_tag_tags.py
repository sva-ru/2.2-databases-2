# Generated by Django 4.2.4 on 2023-08-29 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_rename_title_tag_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='articles',
            new_name='tags',
        ),
    ]