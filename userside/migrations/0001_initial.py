# Generated by Django 3.1.5 on 2021-02-23 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mname', models.CharField(max_length=50)),
                ('mfees', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('utype', models.CharField(max_length=7)),
            ],
        ),
    ]