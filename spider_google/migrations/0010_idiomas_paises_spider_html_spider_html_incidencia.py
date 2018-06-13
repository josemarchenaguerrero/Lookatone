# Generated by Django 2.0.6 on 2018-06-08 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('spider_google', '0009_auto_20180608_2138'),
    ]

    operations = [
        migrations.CreateModel(
            name='idiomas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('reduccion', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='paises',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('reduccion', models.CharField(max_length=2)),
                ('continente', models.CharField(choices=[('America Norte', 'America Norte'), ('America Sur', 'America Sur'), ('America Central', 'America Central'), ('Asia', 'Asia'), ('Europa', 'Europa'), ('Oceania', 'Oceania'), ('Africa', 'Africa'), ('Antartida', 'Antartida')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='spider_html',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filtro', models.CharField(max_length=200)),
                ('subfiltro', models.CharField(max_length=200)),
                ('titulo', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
                ('fecha', models.CharField(editable=False, max_length=10)),
                ('hora', models.CharField(editable=False, max_length=5)),
                ('html', models.FileField(blank=True, upload_to='HTML/')),
            ],
        ),
        migrations.CreateModel(
            name='spider_html_incidencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('incidencia', models.TextField()),
                ('spider_html', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spider_google.spider_html')),
            ],
        ),
    ]
