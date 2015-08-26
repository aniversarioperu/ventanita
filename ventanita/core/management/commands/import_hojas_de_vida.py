# Copyright 2015 by AniversarioPeru. All rights reserved.
# Revisions 2015 copyright by McPollo. All rights reserved.
# This code is part of the Ventanita distribution and governed by its
# license. Please see the LICENSE file that should have been included
# as part of this package.

import codecs
import datetime
import hashlib
from optparse import make_option
import unicodedata

import pyprind
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist

from core.models import Candidato
from core.models import InstitucionEducativa
from core.models import Estudio
from core.utils import get_item_from_list


class Command(BaseCommand):
    """
    Imports TSV data from 'Hojas de vida'
    """
    option_list = BaseCommand.option_list + (
        make_option('--tsvfile',
                    dest='tsvfile',
                    help='Enter name of tsv file as argument.'
                    ),
        make_option('--sheet',
                    dest='sheet',
                    help='Enter name of Excel sheet number to import.'
                    ),
    )

    def __init__(self, *args, **kwargs):
        self.sheet = ''
        super(Command, self).__init__(*args, **kwargs)

    def handle(self, *args, **options):
        if options['tsvfile'] is None or options['sheet'] is None:
            error_msg = 'Enter name of tsv file and sheet number as argument.' \
                        ' "python manage.py import_hojas_de_vida --tsvfile=hoja0.tsv --sheet=0 --settings=ventanita.settings.local'
            raise CommandError(error_msg)

        tsv_file = options['tsvfile']
        sheet = options['sheet']
        self.sheet = sheet

        with codecs.open(tsv_file, "r") as file_handle:
            dump = file_handle.readlines()

        if sheet == '0':
            items = []
            for line in pyprind.prog_bar(dump):
                item = self.parse_line(line)
                if item is not None:
                    items.append(Candidato(**item))
            Candidato.objects.bulk_create(items)
        elif sheet == '1':
            self.import_institucion_educativa(dump)
            self.import_education_for_candidate(dump)
        elif sheet == '2':
            self.import_institucion_educativa_superior(dump)
            self.import_education_for_candidate(dump)

    def import_institucion_educativa(self, dump):
        instituciones = []
        for line in pyprind.prog_bar(dump):
            fields = line.strip().split('\t')

            this_inst_edu = get_institucion_primaria(fields)
            if this_inst_edu not in instituciones:
                instituciones.append(this_inst_edu)

            this_inst_edu = get_institucion_secundaria(fields)
            if this_inst_edu not in instituciones:
                instituciones.append(this_inst_edu)

        upload_instituciones(instituciones)

    def import_education_for_candidate(self, dump):
        estudios = []
        lines = self.convert_to_lines(dump)
        for line in pyprind.prog_bar(
                lines, monitor=True, title="Importing studies for candidate"):
            if self.sheet == '2':
                e = self.construct_education_obj(line, 'superior')
                estudios.append(e)
            elif self.sheet == '1':
                e = self.construct_education_obj(line, 'primaria')
                if e.inicio != '0':
                    estudios.append(e)

                e = self.construct_education_obj(line, 'secundaria')
                if e.inicio != '0':
                    estudios.append(e)

        Estudio.objects.bulk_create(estudios)

    def import_institucion_educativa_superior(self, dump):
        instituciones = []
        lines = self.convert_to_lines(dump)
        for line in pyprind.prog_bar(
                lines, monitor=True, title="Importing high studies for candidate"):
            this_inst_edu = get_institucion_superior(line)
            if this_inst_edu not in instituciones:
                instituciones.append(this_inst_edu)
        upload_instituciones(instituciones)

    def convert_to_lines(self, dump):
        lines = []
        append = lines.append
        for line in dump:
            fields = line.strip().split('\t')
            if fields[1] == 'DNI':
                continue
            append(fields)
        return lines

    def construct_education_obj(self, fields, type):
        candidato = self.get_candidato(fields)
        institucion_ed_obj = self.get_inst_ed(fields, type)
        if type == 'superior':
            educacion_inicio, educacion_fin = get_superior_rango(fields)
            if fields[5] == 'TECNICO':
                tipo_de_estudio = 'tecnica'
            elif fields[5] == 'UNIVERSITARIO':
                tipo_de_estudio = 'universitaria'
            elif fields[5] == 'POST-GRADO':
                tipo_de_estudio = 'postgrado'
            else:
                tipo_de_estudio = ''
            type = tipo_de_estudio
            curso = get_item_from_list(fields, 8)
            carrera = get_item_from_list(fields, 9)
            if fields[11] == 'SI':
                concluido = True
            else:
                concluido = False
            tipo_de_grado = get_item_from_list(fields, 14)
            codigo_anr = get_item_from_list(fields, 15)
            tipo_postgrado = get_item_from_list(fields, 16)
            otro_tipo_documento = get_item_from_list(fields, 17)

            e = Estudio(candidato=candidato, institucion_educativa=institucion_ed_obj, tipo_de_estudio=type,
                        inicio=educacion_inicio, fin=educacion_fin, curso=curso, carrera=carrera,
                        concluido=concluido, tipo_de_grado=tipo_de_grado, codigo_anr=codigo_anr,
                        tipo_postgrado=tipo_postgrado, otro_tipo_documento=otro_tipo_documento)
            return e

        if type == 'primaria':
            educacion_inicio, educacion_fin = self.get_primaria_rango(fields)
        elif type == 'secundaria':
            educacion_inicio, educacion_fin = self.get_secundaria_rango(fields)
        e = Estudio(candidato=candidato, institucion_educativa=institucion_ed_obj,
                    tipo_de_estudio=type, inicio=educacion_inicio, fin=educacion_fin)
        return e

    def get_candidato(self, fields):
        dni = fields[1]
        candidato = Candidato.objects.get(dni=dni)
        return candidato

    def get_inst_ed(self, fields, type):
        if type == 'primaria':
            colegio = get_institucion_primaria(fields)
        elif type == 'secundaria':
            colegio = get_institucion_secundaria(fields)
        elif type == 'superior':
            colegio = get_institucion_superior(fields)
        cole_obj = InstitucionEducativa.objects.filter(sha1=make_sha1(colegio))[0]
        return cole_obj

    def get_primaria_rango(self, fields):
        inicio = get_item_from_list(fields, 7)
        fin = get_item_from_list(fields, 8)
        return inicio, fin

    def get_secundaria_rango(self, fields):
        inicio = get_item_from_list(fields, 9)
        fin = get_item_from_list(fields, 10)
        return inicio, fin

    def parse_line(self, line):
        line = line.strip()
        if line != '':
            fields = line.split('\t')
            item = dict()
            item['dni'] = fields[0]
            item['postulacion_departamento'] = fields[1]
            item['postulacion_provincia'] = fields[2]
            item['postulacion_distrito'] = fields[3]
            item['candidato_jne_id'] = fields[4]
            item['org_politica'] = fields[5]
            item['postulacion_cargo'] = fields[6]
            item['postulacion_designacion'] = fields[7]
            item['apellido_paterno'] = fields[8]
            item['apellido_materno'] = fields[9]
            item['nombres'] = fields[10]
            item['sexo'] = fields[11]
            item['email'] = fields[12]
            item['nacimiento_departamento'] = fields[13]
            item['nacimiento_provincia'] = fields[14]
            item['nacimiento_distrito'] = fields[15]
            try:
                item['nacimiento_fecha'] = datetime.datetime.strptime(fields[16], '%Y%m%d').date()
            except ValueError:
                item['nacimiento_fecha'] = None

            item['residencia_departamento'] = get_item_from_list(fields, 17)
            item['residencia_provincia'] = get_item_from_list(fields, 18)
            item['residencia_distrito'] = get_item_from_list(fields, 19)
            item['residencia_lugar'] = get_item_from_list(fields, 20)
            item['residencia_tiempo'] = get_item_from_list(fields, 21)

            if item['dni'] != 'DNI':
                return item
        return None


def get_superior_rango(fields):
    inicio = get_item_from_list(fields, 12)
    fin = get_item_from_list(fields, 13)
    return inicio, fin


def get_institucion_primaria(fields):
    nombre_primaria = get_item_from_list(fields, 5)
    departamento_primaria = get_item_from_list(fields, 12)
    provincia_primaria = get_item_from_list(fields, 13)
    distrito_primaria = get_item_from_list(fields, 14)
    extranjero = get_item_from_list(fields, 20)
    pais = get_item_from_list(fields, 21)
    item = {
        'nombre': nombre_primaria,
        'departamento': departamento_primaria,
        'provincia': provincia_primaria,
        'distrito': distrito_primaria,
    }
    this_inst_edu = {
        'sha1': make_sha1(item),
        'nombre': nombre_primaria,
        'departamento': departamento_primaria,
        'provincia': provincia_primaria,
        'distrito': distrito_primaria,
        'extranjero': extranjero,
        'pais': pais,
    }
    return this_inst_edu


def get_institucion_secundaria(fields):
    nombre_secundaria = get_item_from_list(fields, 6)
    departamento_secundaria = get_item_from_list(fields, 17)
    provincia_secundaria = get_item_from_list(fields, 18)
    distrito_secundaria = get_item_from_list(fields, 19)
    extranjero = get_item_from_list(fields, 20)
    pais = get_item_from_list(fields, 21)
    item = {
        'nombre': nombre_secundaria,
        'departamento': departamento_secundaria,
        'provincia': provincia_secundaria,
        'distrito': distrito_secundaria,
        }
    this_inst_edu = {
        'sha1': make_sha1(item),
        'nombre': nombre_secundaria,
        'departamento': departamento_secundaria,
        'provincia': provincia_secundaria,
        'distrito': distrito_secundaria,
        'extranjero': extranjero,
        'pais': pais,
    }
    return this_inst_edu


def get_institucion_superior(fields):
    nombre = get_item_from_list(fields, 10)
    departamento = get_item_from_list(fields, 18)
    provincia = get_item_from_list(fields, 19)
    distrito = get_item_from_list(fields, 20)
    extranjero = get_item_from_list(fields, 6)
    pais = get_item_from_list(fields, 7)
    item = {
        'nombre': nombre,
        'departamento': departamento,
        'provincia': provincia,
        'distrito': distrito,
    }
    this_inst_edu = {
        'sha1': make_sha1(item),
        'nombre': nombre,
        'departamento': departamento,
        'provincia': provincia,
        'distrito': distrito,
        'extranjero': extranjero,
        'pais': pais,
    }
    return this_inst_edu


def upload_instituciones(instituciones):
    objs = []
    for i in instituciones:
        this_inst = InstitucionEducativa(**i)
        objs.append(this_inst)
    InstitucionEducativa.objects.bulk_create(objs)


def make_sha1(item):
    hash_input = str(
        str(remove_accents(item['nombre'])) +
        str(remove_accents(item['departamento'])) +
        str(remove_accents(item['provincia']))
    )
    hash_output = hashlib.sha1()
    hash_output.update(hash_input.encode("utf-8"))
    return hash_output.hexdigest()


def remove_accents(input_str):
    nkfd_form = unicodedata.normalize('NFKD', input_str)
    only_ascii = nkfd_form.encode('ASCII', 'ignore')
    return only_ascii
