# Generated by Django 2.2.7 on 2020-01-23 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0022_auto_20200123_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='url',
            name='link',
            field=models.CharField(default='Not Found', max_length=1000, null=True),
        ),
    ]
