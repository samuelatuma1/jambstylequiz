# Generated by Django 3.2 on 2021-04-28 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20210313_0902'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='image',
            field=models.ImageField(blank=True, upload_to='questions/'),
        ),
    ]