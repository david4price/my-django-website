# Generated by Django 4.1.3 on 2022-12-10 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0004_alter_parkingticket_exit_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parkingticket',
            name='enter_time',
            field=models.DateTimeField(null=True),
        ),
    ]
