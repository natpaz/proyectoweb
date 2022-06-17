# Generated by Django 4.0.5 on 2022-06-14 00:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('correo', models.CharField(max_length=50)),
                ('asunto', models.CharField(max_length=50)),
                ('mensaje', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido_paterno', models.CharField(max_length=50)),
                ('apellido_materno', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('telefono', models.CharField(max_length=20)),
                ('domicilio', models.TextField()),
                ('fecha_registro', models.DateTimeField(auto_now=True)),
                ('fecha_nacimiento', models.DateField()),
                ('formulario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Registro.formulario')),
            ],
        ),
    ]