# Generated by Django 5.0.7 on 2024-10-12 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classifiche', '0006_alter_comment_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
