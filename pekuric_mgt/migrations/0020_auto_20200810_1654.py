# Generated by Django 3.0.7 on 2020-08-10 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pekuric_mgt', '0019_auto_20200810_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unicornservice',
            name='service_description',
            field=models.TextField(default=None, help_text='Write your service description here'),
        ),
    ]
