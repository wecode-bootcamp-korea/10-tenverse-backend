# Generated by Django 3.0.7 on 2020-07-27 04:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_subimage_is_hover'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subimage',
            old_name='is_hover',
            new_name='is_hovered',
        ),
    ]
