# Generated by Django 4.2.5 on 2024-01-02 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sale_price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
