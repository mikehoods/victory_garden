# Generated by Django 3.2.4 on 2021-06-08 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]