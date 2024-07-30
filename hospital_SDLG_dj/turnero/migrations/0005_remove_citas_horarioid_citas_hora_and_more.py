# Generated by Django 5.0.6 on 2024-07-28 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turnero', '0004_alter_usuarios_profile_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='citas',
            name='horarioID',
        ),
        migrations.AddField(
            model_name='citas',
            name='hora',
            field=models.TimeField(),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='profile_picture',
            field=models.ImageField(blank=True, default='profile_pictures/default.png', null=True, upload_to='profile_pictures/'),
        ),
    ]
