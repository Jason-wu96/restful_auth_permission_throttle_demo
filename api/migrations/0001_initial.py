# Generated by Django 2.2.6 on 2019-10-31 03:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, unique=True)),
                ('password', models.CharField(max_length=32)),
                ('user_type', models.IntegerField(choices=[(1, '普通用户'), (2, 'vip'), (3, 'suvip')])),
            ],
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=64)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.UserInfo')),
            ],
        ),
    ]
