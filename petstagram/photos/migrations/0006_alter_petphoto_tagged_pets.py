# Generated by Django 5.0.1 on 2024-01-27 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_alter_pet_slug'),
        ('photos', '0005_alter_petphoto_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petphoto',
            name='tagged_pets',
            field=models.ManyToManyField(blank=True, default='No tagged pets', to='pets.pet'),
        ),
    ]
