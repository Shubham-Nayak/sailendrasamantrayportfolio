# Generated by Django 3.0.5 on 2020-08-05 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20200805_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='createdon',
            field=models.DateTimeField(default=''),
        ),
    ]
