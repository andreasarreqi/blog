# Generated by Django 3.2.19 on 2023-05-14 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='sent',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
