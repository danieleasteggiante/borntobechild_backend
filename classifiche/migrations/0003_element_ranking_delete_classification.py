# Generated by Django 5.0.7 on 2024-08-24 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classifiche', '0002_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='element',
            name='ranking',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Classification',
        ),
    ]
