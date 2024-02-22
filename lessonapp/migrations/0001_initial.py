# Generated by Django 5.0.1 on 2024-02-05 05:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_product', models.CharField(max_length=100, unique=True)),
                ('description_product', models.TextField()),
                ('price_product', models.DecimalField(decimal_places=2, max_digits=10)),
                ('number_product', models.PositiveIntegerField()),
                ('date_addition', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=15, unique=True)),
                ('address', models.TextField()),
                ('date_birth', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('general_sum', models.DecimalField(decimal_places=2, max_digits=10)),
                ('formation_date', models.DateTimeField(auto_now_add=True)),
                ('products', models.ManyToManyField(to='lessonapp.product')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lessonapp.user')),
            ],
        ),
    ]
