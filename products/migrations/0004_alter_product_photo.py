# Generated by Django 5.0.7 on 2024-07-22 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_available_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='media', verbose_name='Photo'),
        ),
    ]
