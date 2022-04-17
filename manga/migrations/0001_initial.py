# Generated by Django 4.0.2 on 2022-04-17 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('description', models.TextField(default='')),
                ('slug', models.SlugField(blank=True, default='')),
                ('image', models.ImageField(blank=True, default='', upload_to='images')),
            ],
        ),
    ]
