# Generated by Django 5.1.1 on 2024-09-07 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0003_rename_product_order_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='additional_information',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='takeaway',
            field=models.BooleanField(default=False),
        ),
    ]
