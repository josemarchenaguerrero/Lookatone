# Generated by Django 2.0.3 on 2018-05-16 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spider_google', '0007_auto_20180515_1500'),
    ]

    operations = [
        migrations.CreateModel(
            name='spider_html_incidencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('incidencia', models.TextField()),
                ('spider_html', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spider_google.spider_html')),
            ],
        ),
    ]
