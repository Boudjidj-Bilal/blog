# Generated by Django 4.0.2 on 2023-05-07 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chapitre', '0005_rename_chapitreid_changementcomment_chapitre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageschapitre',
            name='chapitre',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='chapitre.chapitre'),
        ),
    ]