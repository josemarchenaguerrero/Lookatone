# Generated by Django 2.0.3 on 2018-05-02 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spider_google', '0002_auto_20180502_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idiomas',
            name='reduccion',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='paises',
            name='reduccion',
            field=models.CharField(max_length=2),
        ),
    ]