# Generated by Django 5.0.7 on 2024-09-14 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0019_remove_userreview_is_borrowed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userreview',
            name='name',
        ),
    ]
