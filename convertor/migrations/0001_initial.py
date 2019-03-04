# Generated by Django 2.1 on 2019-03-01 13:54

import convertor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('published_date', models.DateTimeField(auto_now_add=True)),
                ('summary', models.TextField(blank=True, max_length=200)),
                ('slug', models.SlugField()),
                ('page_md', models.FileField(upload_to=convertor.models.post_filename)),
                ('page_web', models.FileField(blank=True, null=True, upload_to='')),
            ],
            options={
                'ordering': ['-published_date'],
            },
        ),
    ]
