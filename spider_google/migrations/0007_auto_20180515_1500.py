# Generated by Django 2.0.3 on 2018-05-15 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spider_google', '0006_auto_20180515_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spider_html',
            name='fecha',
            field=models.CharField(editable=False, max_length=10),
        ),
        migrations.AlterField(
            model_name='spider_html',
            name='hora',
            field=models.CharField(editable=False, max_length=5),
        ),
    ]
