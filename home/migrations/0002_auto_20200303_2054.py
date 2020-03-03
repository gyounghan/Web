# Generated by Django 2.2.9 on 2020-03-03 11:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='thumname_image',
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(null=True, upload_to=home.models.user_path),
        ),
        migrations.AlterField(
            model_name='photo',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
