# Generated by Django 5.1.6 on 2025-02-26 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_team_facebook_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='facebook_link',
            field=models.URLField(max_length=100),
        ),
    ]
