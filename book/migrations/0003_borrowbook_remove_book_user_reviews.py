# Generated by Django 5.0.7 on 2024-09-12 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_alter_book_user_reviews'),
    ]

    operations = [
        migrations.CreateModel(
            name='BorrowBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=100)),
                ('book_description', models.TextField()),
                ('book_price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('book_image', models.ImageField(upload_to='')),
                ('is_borrowed', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='user_reviews',
        ),
    ]
