# Generated by Django 5.0.7 on 2024-09-12 13:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('borrowing_price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/uploads/')),
                ('user_reviews', models.TextField()),
                ('book_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.bookcategory')),
            ],
        ),
    ]
