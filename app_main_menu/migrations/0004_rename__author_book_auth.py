# Generated by Django 4.2.10 on 2024-03-13 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_main_menu', '0003_alter_author_id_alter_book_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='_author',
            new_name='auth',
        ),
    ]
