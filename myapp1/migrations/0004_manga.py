# Generated by Django 4.0.2 on 2022-03-09 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0003_flower_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
            ],
        ),
    ]
