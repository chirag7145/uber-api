# Generated by Django 2.0.6 on 2018-06-12 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(help_text='Name', max_length=20)),
                ('username', models.CharField(help_text='UserName', max_length=20, primary_key=True, serialize=False)),
                ('phone_no', models.IntegerField(help_text='Mobile No.')),
                ('aadhar_no', models.IntegerField(help_text='Aadhar Card No.')),
                ('licence_no', models.CharField(help_text='Licence No.', max_length=15)),
                ('car_no', models.CharField(default='', help_text='Car No.', max_length=15)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(help_text='Name', max_length=20)),
                ('username', models.CharField(help_text='UserName', max_length=20, primary_key=True, serialize=False)),
                ('phone_no', models.IntegerField(help_text='Mobile No.')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
