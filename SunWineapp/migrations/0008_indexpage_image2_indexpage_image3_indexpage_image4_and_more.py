# Generated by Django 5.1.4 on 2025-07-28 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SunWineapp', '0007_indexpage_image1_indexpage_title12'),
    ]

    operations = [
        migrations.AddField(
            model_name='indexpage',
            name='image2',
            field=models.ImageField(default='', upload_to=''),
        ),
        migrations.AddField(
            model_name='indexpage',
            name='image3',
            field=models.ImageField(default='', upload_to=''),
        ),
        migrations.AddField(
            model_name='indexpage',
            name='image4',
            field=models.ImageField(default='', upload_to=''),
        ),
        migrations.AddField(
            model_name='indexpage',
            name='image5',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
