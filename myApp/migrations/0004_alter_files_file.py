# Generated by Django 4.1.7 on 2023-06-01 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_alter_files_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]