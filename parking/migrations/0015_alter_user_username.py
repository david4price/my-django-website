# Generated by Django 4.1.3 on 2022-12-11 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0014_alter_user_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
    ]