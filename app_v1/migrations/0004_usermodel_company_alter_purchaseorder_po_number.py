# Generated by Django 5.0.1 on 2024-04-29 07:15

import app_v1.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_v1', '0003_usermodel_priority_alter_purchaseorder_po_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='company',
            field=models.BooleanField(default='False'),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='po_number',
            field=models.CharField(default=app_v1.models.generate_unique_po_number, max_length=5, unique=True),
        ),
    ]