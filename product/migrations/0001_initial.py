# Generated by Django 3.0.7 on 2020-07-28 01:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'colors',
            },
        ),
        migrations.CreateModel(
            name='ColorFilter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'color_filters',
            },
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_detail', models.CharField(max_length=100)),
                ('sub_detail', models.CharField(max_length=500)),
                ('feature', models.CharField(max_length=500)),
                ('feature_image', models.CharField(max_length=300)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'details',
            },
        ),
        migrations.CreateModel(
            name='GenderSegmentation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'gender_segmentation',
            },
        ),
        migrations.CreateModel(
            name='MainCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'main_categories',
            },
        ),
        migrations.CreateModel(
            name='MainImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'main_images',
            },
        ),
        migrations.CreateModel(
            name='Shoe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
            ],
            options={
                'db_table': 'shoes',
            },
        ),
        migrations.CreateModel(
            name='ShoeColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Color')),
                ('image', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.MainImage')),
                ('shoe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Shoe')),
            ],
            options={
                'db_table': 'shoes_colors',
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField()),
            ],
            options={
                'db_table': 'sizes',
            },
        ),
        migrations.CreateModel(
            name='TypeFilter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'type_filters',
            },
        ),
        migrations.CreateModel(
            name='SubImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=300)),
                ('is_hovered', models.BooleanField(default=False)),
                ('shoe_color', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.ShoeColor')),
            ],
            options={
                'db_table': 'sub_images',
            },
        ),
        migrations.CreateModel(
            name='ShoeColorSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('shoe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.ShoeColor')),
                ('size', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Size')),
            ],
            options={
                'db_table': 'shoecolor_sizes',
            },
        ),
        migrations.AddField(
            model_name='shoecolor',
            name='size',
            field=models.ManyToManyField(through='product.ShoeColorSize', to='product.Size'),
        ),
        migrations.CreateModel(
            name='ShoeCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('main_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.MainCategory')),
            ],
            options={
                'db_table': 'shoe_categories',
            },
        ),
        migrations.AddField(
            model_name='shoe',
            name='color',
            field=models.ManyToManyField(through='product.ShoeColor', to='product.Color'),
        ),
        migrations.AddField(
            model_name='shoe',
            name='detail',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Detail'),
        ),
        migrations.AddField(
            model_name='shoe',
            name='gender_segmentation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.GenderSegmentation'),
        ),
        migrations.AddField(
            model_name='shoe',
            name='main_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.MainCategory'),
        ),
        migrations.AddField(
            model_name='shoe',
            name='shoe_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.ShoeCategory'),
        ),
        migrations.AddField(
            model_name='shoe',
            name='type_filter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.TypeFilter'),
        ),
        migrations.AddField(
            model_name='color',
            name='color_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.ColorFilter'),
        ),
    ]
