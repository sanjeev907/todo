# Generated by Django 4.2.2 on 2023-06-08 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]
