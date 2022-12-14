# Generated by Django 4.0.5 on 2022-08-19 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.URLField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('journalist', models.CharField(max_length=10, null=True)),
                ('press', models.CharField(max_length=10, null=True)),
                ('date', models.DateField(null=True)),
                ('section', models.CharField(max_length=10)),
                ('link', models.URLField()),
                ('title', models.CharField(max_length=200)),
                ('main_content', models.TextField()),
                ('summary', models.TextField(null=True)),
                ('views', models.IntegerField(default=0)),
                ('image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='news.newsimage')),
            ],
        ),
    ]
