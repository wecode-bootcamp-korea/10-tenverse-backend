# Generated by Django 3.0.7 on 2020-07-27 23:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20200727_0405'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoeColorSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('shoecolor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.ShoeColor')),
                ('size', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Size')),
            ],
            options={
                'db_table': 'shoecolor_sizes',
            },
        ),
        migrations.RemoveField(
            model_name='shoe',
            name='size',
        ),
        migrations.DeleteModel(
            name='ShoeSize',
        ),
        migrations.AddField(
            model_name='shoecolor',
            name='size',
            field=models.ManyToManyField(through='product.ShoeColorSize', to='product.Size'),
        ),
    ]
