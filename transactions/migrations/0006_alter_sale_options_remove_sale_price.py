# Generated by Django 5.0.6 on 2024-06-13 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0005_alter_sale_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sale',
            options={'verbose_name_plural': 'Sales'},
        ),
        migrations.RemoveField(
            model_name='sale',
            name='price',
        ),
    ]
