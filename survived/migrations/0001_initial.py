# Generated by Django 3.0.4 on 2020-03-31 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Survived',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(default='none', max_length=200)),
                ('country', models.CharField(default='none', max_length=200)),
                ('last_update', models.DateTimeField(default='2019-11-01 00:00:00')),
                ('confirmed', models.IntegerField(default=0)),
                ('deaths', models.IntegerField(default=0)),
                ('recovered', models.IntegerField(default=0)),
                ('active', models.IntegerField(default=0)),
                ('filler', models.IntegerField(default=0)),
            ],
        ),
    ]
