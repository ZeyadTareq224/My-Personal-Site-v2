# Generated by Django 4.1.2 on 2022-11-05 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_project_resume_created_at_resume_updated_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='achievments')),
                ('created_at', models.DateTimeField()),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
