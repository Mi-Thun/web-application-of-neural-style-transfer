# Generated by Django 4.0.2 on 2022-04-14 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='result_image',
            field=models.ImageField(upload_to='files/result'),
        ),
        migrations.AlterField(
            model_name='image',
            name='source_image',
            field=models.ImageField(upload_to='files/source'),
        ),
        migrations.AlterField(
            model_name='image',
            name='style_image',
            field=models.ImageField(upload_to='files/style'),
        ),
    ]