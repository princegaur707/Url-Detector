# Generated by Django 3.0 on 2020-01-25 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userfeedback',
            name='empty',
            field=models.BooleanField(default=False),
        ),
    ]
