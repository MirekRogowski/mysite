# Generated by Django 4.0.2 on 2022-02-15 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_newsletter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
    ]