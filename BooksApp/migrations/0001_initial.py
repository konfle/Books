# Generated by Django 3.1.1 on 2020-10-14 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('published_date', models.CharField(max_length=4)),
                ('isbn_number', models.CharField(max_length=10)),
                ('page_count', models.PositiveSmallIntegerField(max_length=4)),
                ('cover_link', models.URLField()),
                ('language', models.CharField(max_length=10)),
            ],
        ),
    ]