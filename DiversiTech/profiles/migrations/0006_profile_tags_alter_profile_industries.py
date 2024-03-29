# Generated by Django 5.0.3 on 2024-03-26 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tagged_profiles', to='profiles.tag'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='industries',
            field=models.ManyToManyField(blank=True, related_name='industry_profiles', to='profiles.industry'),
        ),
    ]
