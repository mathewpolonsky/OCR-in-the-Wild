# Generated by Django 4.1.2 on 2022-10-26 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_alter_image_recognized_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='recognized_text',
            field=models.CharField(blank=True, default='test', max_length=100),
        ),
    ]
