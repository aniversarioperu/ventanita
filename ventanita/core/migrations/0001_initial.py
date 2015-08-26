# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BienInmueble',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('registro', models.CharField(max_length=300)),
                ('valor', models.IntegerField()),
                ('tipo', models.CharField(max_length=300)),
                ('direccion', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='BienMueble',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('bien', models.CharField(max_length=300)),
                ('tipo', models.CharField(max_length=300)),
                ('descripcion', models.CharField(max_length=300)),
                ('caracteristicas', models.CharField(max_length=300)),
                ('valor', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('candidato_jne_id', models.IntegerField(help_text='ID asignado por el JNE')),
                ('dni', models.CharField(primary_key=True, max_length=8, serialize=False)),
                ('nombres', models.CharField(max_length=300)),
                ('apellido_materno', models.CharField(max_length=300)),
                ('apellido_paterno', models.CharField(max_length=300)),
                ('sexo', models.CharField(max_length=300)),
                ('email', models.CharField(max_length=300)),
                ('org_politica', models.CharField(max_length=300)),
                ('madre', models.CharField(max_length=300)),
                ('conyuge', models.CharField(max_length=300)),
                ('padre', models.CharField(max_length=300)),
                ('postulacion_cargo', models.CharField(max_length=300)),
                ('postulacion_ubigeo', models.CharField(max_length=300)),
                ('postulacion_distrito', models.CharField(max_length=300)),
                ('postulacion_provincia', models.CharField(max_length=300)),
                ('postulacion_departamento', models.CharField(max_length=300)),
                ('postulacion_designacion', models.TextField()),
                ('nacimiento_pais', models.CharField(max_length=300)),
                ('nacimiento_ubigeo', models.CharField(max_length=300)),
                ('nacimiento_fecha', models.DateField(blank=True, null=True)),
                ('nacimiento_distrito', models.CharField(max_length=300)),
                ('nacimiento_provincia', models.CharField(max_length=300)),
                ('nacimiento_departamento', models.CharField(max_length=300)),
                ('residencia_lugar', models.TextField(blank=True)),
                ('residencia_ubigeo', models.CharField(max_length=300, blank=True)),
                ('residencia_distrito', models.CharField(max_length=300, blank=True)),
                ('residencia_tiempo', models.CharField(max_length=300, blank=True)),
                ('residencia_provincia', models.CharField(max_length=300, blank=True)),
                ('residencia_departamento', models.CharField(max_length=300, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Civil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('expediente', models.CharField(max_length=300)),
                ('juzgado', models.CharField(max_length=300)),
                ('materia', models.CharField(max_length=300)),
                ('fallo', models.CharField(max_length=300)),
                ('candidato', models.ForeignKey(to='core.Candidato')),
            ],
        ),
        migrations.CreateModel(
            name='DeudorRedam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('dni', models.TextField()),
                ('paternal_surname', models.TextField()),
                ('maternal_surname', models.TextField()),
                ('given_names', models.TextField()),
                ('url', models.URLField()),
                ('debt', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='DeudorRedamBond',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('bond_type', models.TextField()),
                ('full_name', models.TextField()),
                ('debtor', models.ForeignKey(to='core.DeudorRedam')),
            ],
        ),
        migrations.CreateModel(
            name='Eleccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('proceso_electoral', models.CharField(max_length=300)),
                ('cargo', models.CharField(max_length=300)),
                ('provincia', models.CharField(max_length=300)),
                ('departamento', models.CharField(max_length=300)),
                ('inicio', models.IntegerField()),
                ('fin', models.IntegerField()),
                ('distrito', models.CharField(max_length=300)),
                ('ambito', models.CharField(max_length=300)),
                ('org_politica', models.CharField(max_length=300)),
                ('candidato', models.ForeignKey(to='core.Candidato')),
            ],
        ),
        migrations.CreateModel(
            name='Estudio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('tipo_de_estudio', models.CharField(choices=[('primaria', 'primaria'), ('tecnica', 'tecnica'), ('secundaria', 'secundaria'), ('universitaria', 'universitaria'), ('postgrado', 'postgrado')], help_text='Colegio, instituto, universidad y grado de instrucción.', max_length=300, blank=True)),
                ('concluido', models.NullBooleanField()),
                ('inicio', models.IntegerField()),
                ('fin', models.IntegerField()),
                ('codigo_anr', models.TextField(blank=True)),
                ('curso', models.CharField(help_text='Nombre de estudio', max_length=300)),
                ('especialidad', models.CharField(max_length=300)),
                ('grado_titulo', models.CharField(max_length=300)),
                ('facultad', models.CharField(max_length=300)),
                ('carrera', models.CharField(max_length=300)),
                ('tipo_de_grado', models.TextField(blank=True)),
                ('tipo_postgrado', models.TextField(blank=True)),
                ('otro_tipo_documento', models.TextField(blank=True)),
                ('candidato', models.ForeignKey(to='core.Candidato')),
            ],
        ),
        migrations.CreateModel(
            name='Experiencia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('sector', models.CharField(max_length=300)),
                ('cargo', models.IntegerField()),
                ('provincia', models.CharField(max_length=300)),
                ('empleador', models.CharField(max_length=300)),
                ('distrito', models.CharField(max_length=300)),
                ('inicio', models.IntegerField()),
                ('fin', models.IntegerField()),
                ('departamento', models.CharField(max_length=300)),
                ('candidato', models.ForeignKey(to='core.Candidato')),
            ],
        ),
        migrations.CreateModel(
            name='InstitucionEducativa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('sha1', models.CharField(help_text='This is only used when importing data.', db_index=True, max_length=40)),
                ('nombre', models.CharField(max_length=300)),
                ('pais', models.CharField(max_length=300)),
                ('extranjero', models.CharField(max_length=300)),
                ('departamento', models.CharField(max_length=300)),
                ('provincia', models.CharField(max_length=300)),
                ('distrito', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Militancia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('inicio', models.IntegerField()),
                ('fin', models.IntegerField()),
                ('org_politica', models.CharField(max_length=300)),
                ('candidato', models.ForeignKey(to='core.Candidato')),
            ],
        ),
        migrations.CreateModel(
            name='Observacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('referencia', models.CharField(max_length=300)),
                ('anotacion', models.CharField(max_length=2000)),
                ('candidato', models.ForeignKey(to='core.Candidato')),
            ],
        ),
        migrations.CreateModel(
            name='OtraExperiencia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('cargo', models.CharField(max_length=300)),
                ('entidad', models.CharField(max_length=300)),
                ('inicio', models.IntegerField()),
                ('fin', models.IntegerField()),
                ('candidato', models.ForeignKey(to='core.Candidato')),
            ],
        ),
        migrations.CreateModel(
            name='Partidario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('cargo', models.CharField(max_length=300)),
                ('ambito', models.CharField(max_length=300)),
                ('org_politica', models.CharField(max_length=300)),
                ('inicio', models.IntegerField()),
                ('fin', models.IntegerField()),
                ('candidato', models.ForeignKey(to='core.Candidato')),
            ],
        ),
        migrations.CreateModel(
            name='Penal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('delito', models.CharField(max_length=300)),
                ('expediente', models.CharField(max_length=300)),
                ('juzgado', models.CharField(max_length=300)),
                ('fallo', models.CharField(max_length=300)),
                ('fecha_sentencia', models.DateField()),
                ('candidato', models.ForeignKey(to='core.Candidato')),
            ],
        ),
        migrations.AddField(
            model_name='estudio',
            name='institucion_educativa',
            field=models.ForeignKey(to='core.InstitucionEducativa'),
        ),
        migrations.AddField(
            model_name='bienmueble',
            name='candidato',
            field=models.ForeignKey(to='core.Candidato'),
        ),
        migrations.AddField(
            model_name='bieninmueble',
            name='candidato',
            field=models.ForeignKey(to='core.Candidato'),
        ),
    ]
