# Generated by Django 4.1.2 on 2022-10-26 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_rename_images_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='recognized_text',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]