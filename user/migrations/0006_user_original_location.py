# Generated by Django 3.2.9 on 2021-12-24 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_user_zipcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='original_location',
            field=models.TextField(null=True),
        ),
    ]
