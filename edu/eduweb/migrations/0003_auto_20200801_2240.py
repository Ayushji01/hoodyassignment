# Generated by Django 3.0.8 on 2020-08-01 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eduweb', '0002_auto_20200801_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='price',
            field=models.BooleanField(default=False),
        ),
    ]
