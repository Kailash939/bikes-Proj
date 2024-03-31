# Generated by Django 4.0 on 2024-03-20 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bikes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('engine', models.CharField(max_length=40)),
                ('milage', models.IntegerField()),
                ('price', models.FloatField()),
            ],
        ),
    ]
