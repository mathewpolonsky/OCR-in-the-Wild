# Generated by Django 4.1.2 on 2022-10-27 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0004_alter_image_recognized_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='recognized_text',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]