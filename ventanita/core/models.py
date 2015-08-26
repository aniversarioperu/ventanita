# Copyright 2015 by Pedro Muñoz del Rio (pmunozdelrio). All rights reserved.
# Copyright 2015 by Pedro Palacios (Wesitos). All rights reserved.
# Revisions 2015 copyright by AniversarioPeru. All rights reserved.
# This code is part of the Ventanita distribution and governed by its
# license. Please see the LICENSE file that should have been included
# as part of this package.

from django.db import models


GENDER = (
    ('M', 'Male'),
    ('F', 'Female'),
)

""
class TipoMedioContacto(models.Model):
    nombre = models.CharField(max_length=50)


class TipoBienMueble(models.Model):
    nombre = models.CharField(max_length=50)


class TipoBienInmueble(models.Model):
    nombre = models.CharField(max_length=50)


class OtraExperiencia(models.Model):
    cargo = models.CharField(max_length=300)
    entidad = models.CharField(max_length=300)
    inicio = models.IntegerField()
    fin = models.IntegerField()
    candidato = models.ForeignKey('Candidato')


class Militancia(models.Model):
    inicio = models.IntegerField()
    fin = models.IntegerField()
    org_politica = models.CharField(max_length=300)
    candidato = models.ForeignKey('Candidato')


class Civil(models.Model):
    """Antecedentes civiles"""
    expediente = models.CharField(max_length=300)
    juzgado = models.CharField(max_length=300)
    materia = models.CharField(max_length=300)
    fallo = models.CharField(max_length=300)
    candidato = models.ForeignKey('Candidato')


class Penal(models.Model):
    """Antecedentes penales"""
    delito = models.CharField(max_length=300)
    expediente = models.CharField(max_length=300)
    juzgado = models.CharField(max_length=300)
    fallo = models.CharField(max_length=300)
    fecha_sentencia = models.DateField()
    candidato = models.ForeignKey('Candidato', null=True)


class Partidario(models.Model):
    cargo = models.CharField(max_length=300)
    ambito = models.CharField(max_length=300)
    org_politica = models.CharField(max_length=300)
    inicio = models.IntegerField()
    fin = models.IntegerField()
    candidato = models.ForeignKey('Candidato', null=True)


class Eleccion(models.Model):
    proceso_electoral = models.CharField(max_length=300)
    cargo = models.CharField(max_length=300)
    provincia = models.CharField(max_length=300)
    departamento = models.CharField(max_length=300)
    inicio = models.IntegerField()
    fin = models.IntegerField()
    distrito = models.CharField(max_length=300)
    ambito = models.CharField(max_length=300)
    org_politica = models.CharField(max_length=300)
    candidato = models.ForeignKey('Candidato', null=True)


class Sector(models.Model):
    nombre = models.CharField(max_length=50)

class CentroTrabajo(models.Model):
    nombre = models.CharField(max_length=100)
    sector = models.ForeignKey(Sector)

class TipoGradoAcademico(models.Model):
    nombre = models.CharField(max_length=50)

class TipoInstitucionEducativa(models.Model):
    nombre = models.CharField(max_length=40)
    grado_academico = models.ManyToManyField(TipoGradoAcademico)


class InstitucionEducativa(models.Model):
    tipo_institucion_educativa = models.ForeignKey(TipoInstitucionEducativa, null=True)
    sha1 = models.CharField(max_length=40, db_index=True,
                            help_text='This is only used when importing data.')
    nombre = models.CharField(max_length=300)
    pais = models.CharField(max_length=300)
    extranjero = models.CharField(max_length=300)
    departamento = models.CharField(max_length=300)
    provincia = models.CharField(max_length=300)
    distrito = models.CharField(max_length=300)


class Candidato(models.Model):
    candidato_jne_id = models.IntegerField(help_text='ID asignado por el JNE')

    # Datos Personales
    dni = models.CharField(max_length=8, primary_key=True)
    nombres = models.CharField(max_length=300)
    apellido_materno = models.CharField(max_length=300)
    apellido_paterno = models.CharField(max_length=300)
    sexo = models.CharField(max_length=2,
                            choices=GENDER,
                            default='M')


    org_politica = models.CharField(max_length=300)

    medio_contacto = models.ManyToManyField(TipoMedioContacto, through='MedioContacto')

    # Familia
    madre = models.CharField(max_length=300)
    conyuge = models.CharField(max_length=300)
    padre = models.CharField(max_length=300)

    # Postulacion
    postulacion_cargo = models.CharField(max_length=300)
    postulacion_ubigeo = models.CharField(max_length=300)
    postulacion_distrito = models.CharField(max_length=300)
    postulacion_provincia = models.CharField(max_length=300)
    postulacion_departamento = models.CharField(max_length=300)
    postulacion_designacion = models.TextField()

    # Nacimiento
    nacimiento_pais = models.CharField(max_length=300)
    nacimiento_ubigeo = models.CharField(max_length=300)
    nacimiento_fecha = models.DateField(null=True, blank=True)
    nacimiento_distrito = models.CharField(max_length=300)
    nacimiento_provincia = models.CharField(max_length=300)
    nacimiento_departamento = models.CharField(max_length=300)

    # Residencia
    residencia_lugar = models.TextField(blank=True)
    residencia_ubigeo = models.CharField(max_length=300, blank=True)
    residencia_distrito = models.CharField(max_length=300, blank=True)
    residencia_tiempo = models.CharField(max_length=300, blank=True)
    residencia_provincia = models.CharField(max_length=300, blank=True)
    residencia_departamento = models.CharField(max_length=300, blank=True)

    estudios = models.ManyToManyField(InstitucionEducativa, through='Estudio')
    #trabajos = models.ManyToManyField(CentroTrabajo, through='ExperienciaLaboral')

    # bienes_muebles = relationship("BienMueble", backref="candidato")
    # bienes_inmuebles = relationship("BienInmueble", backref="candidato")
    # otra_experiencia = relationship("OtraExperiencia", backref="candidato")
    # militancia = relationship("Militancia", backref="candidato")
    # civil = relationship("Civil", backref="candidato")

    # partidario = relationship("Partidario", backref="candidato")
    # eleccion = relationship("Eleccion", backref="candidato")
    # experiencia = relationship("Experiencia", backref="candidato")
    # observaciones = relationship("Observacion", backref="candidato")


class BienMueble(models.Model):
    nombre = models.CharField(max_length=300)
    tipo_bien = models.ForeignKey(TipoBienMueble, null=True)
    descripcion = models.CharField(max_length=300)
    caracteristicas = models.CharField(max_length=300)
    valor = models.IntegerField()
    candidato = models.ForeignKey(Candidato, null=True)


class BienInmueble(models.Model):
    registro = models.CharField(max_length=300)
    valor = models.IntegerField()
    tipo_bien = models.ForeignKey(TipoBienInmueble, null=True)
    direccion = models.CharField(max_length=300)
    candidato = models.ForeignKey(Candidato, null=True)


class Estudio(models.Model):
    institucion_educativa = models.ForeignKey(InstitucionEducativa)
    tipo_de_estudio = models.ForeignKey(TipoGradoAcademico, null=True)
    candidato = models.ForeignKey(Candidato, null=True)
    concluido = models.NullBooleanField()
    inicio = models.DateField()
    fin = models.DateField()
    codigo_anr = models.TextField(blank=True)


class MedioContacto(models.Model):
    tipo_medio = models.ForeignKey(TipoMedioContacto, null=True)
    candidato = models.ForeignKey(Candidato, null=True)
    contacto = models.CharField(max_length=50)


class ExperienciaLaboral(models.Model):
    cargo = models.CharField(max_length=100)
    departamento = models.CharField(max_length=300)
    provincia = models.CharField(max_length=300)
    distrito = models.CharField(max_length=300)
    empleador = models.ForeignKey(CentroTrabajo, null=True)
    candidato = models.ForeignKey(Candidato, null=True)
    inicio = models.DateField()
    fin = models.DateField()


class Observacion(models.Model):
    referencia = models.CharField(max_length=300)
    anotacion = models.CharField(max_length=2000)
    candidato = models.ForeignKey('Candidato', null=True)


# Registro de morosos por alimentos. REDAM.
class DeudorRedam(models.Model):
    """Demandado"""
    dni = models.TextField()
    paternal_surname = models.TextField()
    maternal_surname = models.TextField()
    given_names = models.TextField()
    url = models.URLField()
    debt = models.FloatField()


class DeudorRedamBond(models.Model):
    """Demandante"""
    debtor = models.ForeignKey('DeudorRedam', null=True)
    bond_type = models.TextField()
    full_name = models.TextField()
