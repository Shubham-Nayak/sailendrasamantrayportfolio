# Generated by Django 3.0.5 on 2020-07-28 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=300)),
                ('subject', models.CharField(default='', max_length=3000)),
                ('query', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
