# Generated by Django 3.2.9 on 2021-12-08 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20211208_0317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author_name',
        ),
        migrations.RemoveField(
            model_name='post',
            name='author_picture_link',
        ),
    ]
