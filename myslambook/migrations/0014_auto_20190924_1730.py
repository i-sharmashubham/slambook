# Generated by Django 2.2.5 on 2019-09-24 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myslambook', '0013_auto_20190924_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slam',
            name='photo',
            field=models.ImageField(upload_to=''),
        ),
    ]
