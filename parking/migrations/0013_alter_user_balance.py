# Generated by Django 4.1.3 on 2022-12-11 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0012_alter_user_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='balance',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
    ]