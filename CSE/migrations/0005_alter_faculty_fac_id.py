# Generated by Django 4.1.4 on 2023-01-28 14:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('CSE', '0004_alter_faculty_fac_id_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='fac_id',
            field=models.UUIDField(default=uuid.UUID('2678accc-a6ca-408d-84f4-68b8fae66e1b'), editable='false', primary_key=True, serialize=False),
        ),
    ]
