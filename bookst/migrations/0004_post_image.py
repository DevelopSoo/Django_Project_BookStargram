# Generated by Django 3.1.6 on 2021-02-11 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookst', '0003_post__type'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='bookst/image'),
        ),
    ]
