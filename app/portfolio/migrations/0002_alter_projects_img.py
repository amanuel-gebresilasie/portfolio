# Generated by Django 4.1.4 on 2022-12-26 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='img',
            field=models.ImageField(upload_to=''),
        ),
    ]
