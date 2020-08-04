# Generated by Django 3.0.8 on 2020-08-03 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookroom', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookroom',
            old_name='date',
            new_name='check_in_date',
        ),
        migrations.AddField(
            model_name='bookroom',
            name='check_out_date',
            field=models.DateField(default='2020-01-01'),
        ),
        migrations.AddField(
            model_name='bookroom',
            name='room_number',
            field=models.IntegerField(default=0),
        ),
    ]