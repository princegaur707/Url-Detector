# Generated by Django 3.0 on 2020-01-25 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20200125_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='userfeedback',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
