# Generated by Django 5.0.1 on 2024-01-27 15:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0004_alter_petphoto_description_alter_petphoto_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petphoto',
            name='description',
            field=models.TextField(default='tetetetetete', max_length=300, validators=[django.core.validators.MinLengthValidator(limit_value=10)]),
            preserve_default=False,
        ),
    ]
