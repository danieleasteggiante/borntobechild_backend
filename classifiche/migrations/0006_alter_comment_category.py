# Generated by Django 5.0.7 on 2024-10-11 07:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classifiche', '0005_remove_category_slug_remove_element_ranking_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='classifiche.category'),
            preserve_default=False,
        ),
    ]
