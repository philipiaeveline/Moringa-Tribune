# Generated by Django 3.1.5 on 2021-01-09 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_editor_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.ImageField(blank=True, upload_to='articles/'),
        ),
    ]
