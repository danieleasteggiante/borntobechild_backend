# Generated by Django 5.0.7 on 2024-10-10 09:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_article_banner_alter_section_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='articles',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='blog.article'),
        ),
    ]