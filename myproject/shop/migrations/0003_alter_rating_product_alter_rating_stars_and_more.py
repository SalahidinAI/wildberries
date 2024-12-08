# Generated by Django 5.1.3 on 2024-12-05 06:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_rename_video_product_product_video_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='shop.product'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='stars',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='shop.product'),
        ),
    ]
