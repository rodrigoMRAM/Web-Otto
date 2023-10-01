# Generated by Django 4.0.6 on 2023-10-01 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre de cliente')),
                ('patente', models.CharField(max_length=20, verbose_name='Patente')),
                ('mes', models.CharField(choices=[('enero', 'Enero'), ('febrero', 'Febrero'), ('marzo', 'Marzo'), ('abril', 'Abril'), ('mayo', 'Mayo'), ('junio', 'Junio'), ('julio', 'Julio'), ('agosto', 'Gato'), ('septiembre', 'Septiembre'), ('octubre', 'Octubre'), ('noviembre', 'Noviembre'), ('diciembre', 'Diciembre')], max_length=50, verbose_name='Fecha')),
                ('dia', models.PositiveIntegerField()),
                ('age', models.IntegerField()),
                ('detalles', models.CharField(max_length=150, verbose_name='Detalles ')),
                ('total', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
