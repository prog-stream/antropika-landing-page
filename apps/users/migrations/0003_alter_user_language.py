# Generated by Django 5.0.5 on 2025-02-20 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='language',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
