# Generated by Django 3.2.9 on 2021-12-04 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
