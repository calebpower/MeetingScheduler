# Generated by Django 3.0.2 on 2020-04-19 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meeting', '0014_meetingtime_hasvoted'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='final_date',
            field=models.CharField(default='TBA', max_length=100),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='location',
            field=models.CharField(default='TBA', max_length=200),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='optional_members',
            field=models.CharField(default='Required', max_length=200),
        ),
    ]
