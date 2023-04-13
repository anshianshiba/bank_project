# Generated by Django 4.1.2 on 2023-04-13 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('dob', models.DateField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=30)),
                ('phonenumber', models.IntegerField()),
                ('email', models.EmailField(max_length=250)),
                ('address', models.CharField(max_length=500)),
                ('district', models.CharField(max_length=250)),
                ('branch', models.CharField(max_length=250)),
                ('acc_type', models.CharField(max_length=250)),
                ('materials', models.CharField(max_length=250)),
            ],
        ),
    ]
