# Generated by Django 5.0.7 on 2024-11-16 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('commentType', models.CharField(max_length=100)),
                ('relatedReference', models.CharField(db_index=True, max_length=100)),
            ],
        ),
    ]