# Generated by Django 2.2.5 on 2019-09-24 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myslambook', '0014_auto_20190924_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slam',
            name='photo',
            field=models.FileField(upload_to=''),
        ),
    ]
