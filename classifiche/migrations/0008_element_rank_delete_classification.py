# Generated by Django 5.0.7 on 2024-10-12 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classifiche', '0007_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='element',
            name='rank',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Classification',
        ),
    ]
