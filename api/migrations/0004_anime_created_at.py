# Generated by Django 5.1.2 on 2024-10-26 21:05

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_anime_character_roles_anime_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
