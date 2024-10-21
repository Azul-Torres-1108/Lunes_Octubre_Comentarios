# Generated by Django 5.1.1 on 2024-10-15 17:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumno', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Frase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField(max_length=400, verbose_name='comentario')),
                ('Alumno_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alumno.alumno')),
            ],
        ),
    ]
