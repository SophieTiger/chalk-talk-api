# Generated by Django 5.1.3 on 2024-11-12 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='crossfit_experience',
            field=models.CharField(choices=[('Newbie', 'Newbie'), ('1-3 years', '1-3 years'), ('3-5 years', '3-5 years'), ('5-8 years', '5-8 years'), ('8-10 years', '8-10 years'), ('OG', 'OG')], default='Newbie', max_length=30),
        ),
    ]