# Generated by Django 4.1.2 on 2022-11-06 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
