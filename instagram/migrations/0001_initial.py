# Generated by Django 3.0.7 on 2020-07-29 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instagram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('user_profile_image', models.URLField(max_length=300)),
                ('image', models.URLField(max_length=300)),
                ('text', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'instagram',
            },
        ),
    ]
