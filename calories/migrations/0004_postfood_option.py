# Generated by Django 4.1.5 on 2023-01-27 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calories', '0003_profile_meal'),
    ]

    operations = [
        migrations.AddField(
            model_name='postfood',
            name='option',
            field=models.CharField(default='صبحانه', max_length=50),
        ),
    ]
