# Generated by Django 3.2.5 on 2021-07-24 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meta',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/images'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='static/images'),
        ),
    ]
