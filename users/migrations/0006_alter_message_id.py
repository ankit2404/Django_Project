# Generated by Django 3.2.9 on 2021-11-27 15:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True),
        ),
    ]