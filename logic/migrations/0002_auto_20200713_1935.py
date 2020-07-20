# Generated by Django 3.0.8 on 2020-07-13 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='asong',
            name='thumb',
            field=models.ImageField(default=0, upload_to='pics'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='asong',
            name='aud',
            field=models.FileField(upload_to='songs'),
        ),
        migrations.AlterField(
            model_name='vsong',
            name='thumb',
            field=models.ImageField(upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='vsong',
            name='vid',
            field=models.FileField(upload_to='vids'),
        ),
    ]