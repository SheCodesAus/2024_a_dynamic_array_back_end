# Generated by Django 5.0.3 on 2024-03-20 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='accepted_terms',
            field=models.BooleanField(default=False),
        ),
    ]
