# Generated by Django 5.0.6 on 2024-07-04 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turnero', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='turnos',
            old_name='TurnoID',
            new_name='turnoID',
        ),
        migrations.AlterField(
            model_name='turnos',
            name='fecha',
            field=models.DateField(),
        ),
    ]
