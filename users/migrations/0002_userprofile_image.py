# Generated by Django 4.2.5 on 2024-10-11 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default=1, upload_to='users'),
            preserve_default=False,
        ),
    ]
