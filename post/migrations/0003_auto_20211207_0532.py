# Generated by Django 3.2.9 on 2021-12-07 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20211207_0531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='trade_description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='wanted_description',
            field=models.TextField(null=True),
        ),
    ]
