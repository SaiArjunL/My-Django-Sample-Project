# Generated by Django 3.0.3 on 2020-08-18 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=264, unique=True)),
                ('last_name', models.CharField(max_length=264, unique=True)),
                ('email_id', models.EmailField(max_length=264, unique=True)),
            ],
        ),
    ]
