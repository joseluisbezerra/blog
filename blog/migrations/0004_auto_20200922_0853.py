# Generated by Django 3.1.1 on 2020-09-22 11:53

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200910_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to=blog.models.imagem_directory_path),
        ),
    ]
