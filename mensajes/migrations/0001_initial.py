# Generated by Django 2.0.6 on 2018-06-09 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mensajes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default=' ', max_length=250)),
                ('correo', models.CharField(default=' ', max_length=250)),
                ('sugerencia', models.CharField(default='', max_length=2000)),
            ],
        ),
    ]
