# Generated by Django 5.0.3 on 2024-03-26 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_industry_profile_industries'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='industries',
            field=models.ManyToManyField(blank=True, related_name='profiles', to='profiles.industry'),
        ),
    ]
