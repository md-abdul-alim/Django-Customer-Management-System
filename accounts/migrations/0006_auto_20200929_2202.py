# Generated by Django 3.1.1 on 2020-09-29 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20200929_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_created',
            field=models.DateTimeField(max_length=200, null=True),
        ),
    ]
