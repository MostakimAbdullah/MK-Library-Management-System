# Generated by Django 5.0.7 on 2024-09-13 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_borrowbook_book_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookcategory',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
