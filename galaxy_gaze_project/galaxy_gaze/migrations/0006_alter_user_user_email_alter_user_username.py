# Generated by Django 4.2.3 on 2023-07-31 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galaxy_gaze', '0005_rename_object_position_deepspaceobject_object_position_dec_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=100),
        ),
    ]
