# Generated by Django 2.0.6 on 2018-06-08 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spider_google', '0008_spider_html_incidencia'),
    ]

    operations = [
        migrations.DeleteModel(
            name='idiomas',
        ),
        migrations.DeleteModel(
            name='paises',
        ),
        migrations.RemoveField(
            model_name='spider_html_incidencia',
            name='spider_html',
        ),
        migrations.DeleteModel(
            name='spider_html',
        ),
        migrations.DeleteModel(
            name='spider_html_incidencia',
        ),
    ]
