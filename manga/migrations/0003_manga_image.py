# Generated by Django 4.0.2 on 2022-04-02 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0002_delete_commentairechapitre'),
    ]

    operations = [
        migrations.AddField(
            model_name='manga',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='images'),
        ),
    ]
