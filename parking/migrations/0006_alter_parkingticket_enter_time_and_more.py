# Generated by Django 4.1.3 on 2022-12-10 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0005_alter_parkingticket_enter_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parkingticket',
            name='enter_time',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='parkingticket',
            name='exit_time',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
