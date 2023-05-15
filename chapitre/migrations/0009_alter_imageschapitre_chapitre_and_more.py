# Generated by Django 4.0.2 on 2023-05-07 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chapitre', '0008_alter_imageschapitre_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageschapitre',
            name='chapitre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='chapitre.chapitre'),
        ),
        migrations.AlterField(
            model_name='imageschapitre',
            name='order',
            field=models.IntegerField(blank=True, default=20000),
        ),
    ]