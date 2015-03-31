# Copyright 2015 by Vitoko. All rights reserved.
# This code is part of the Ventanita distribution and governed by its
# license. Please see the LICENSE file that should have been included
# as part of this package.

import _mssql
import csv
import datetime

def replace_date(date_string):
    if(date_string != ''):
        return datetime.datetime.strptime(date_string, '%Y%m%d')


def replace_quote(content):
    if content != '':
        return content.replace("'", "")


def replace_empty(content):
    if (content == '' or content == 'None'):
        return 0
    else:
        return content


def importar(row):
    conn = _mssql.connect(server='s10.winhost.com:1433',
                          user='DB_76507_ventanita_user',
                          password='123abc$',
                          database='DB_76507_ventanita')
    query = "INSERT INTO Candidatos VALUES('{0}', '{1}', '{2}', '{3}', {4}, '{5}', '{6}', '{7}', '{8}', '{9}', '{10}', '{11}', '{12}', '{13}', '{14}', '{15}', '{16}', '{17}', '{18}', '{19}', '{20}', {21})".format(
        replace_quote(row['DNI']),
        replace_quote(row['DEPARTAMENTO AL QUE POSTULA']),
        replace_quote(row['PROVINCIA AL QUE POSTULA']),
        replace_quote(row['DISTRITO AL QUE POSTULA']),
        replace_quote(row['ID_CANDIDATO']),
        replace_quote(row['NOMBRE COMPLETO']),
        replace_quote(row['ORGANIZACION POLITICA']),
        replace_quote(row['CARGO AL QUE POSTULA']),
        replace_quote(row['DESIGNACION']),
        replace_quote(row['APELLIDO PATERNO']),
        replace_quote(row['APELLIDO MATERNO']),
        replace_quote(row['SEXO']),
        replace_quote(row['CORREO ELECTRONICO']),
        replace_quote(row['DEPARTAMENTO DE NACIMIENTO']),
        replace_quote(row['PROVINCIA DE NACIMIENTO']),
        replace_quote(row['DISTRITO DE NACIMIENTO']),
        replace_date(row['FECHA DE NACIMIENTO']),
        replace_quote(row['DEPARTAMENTO DE RESIDENCIA']),
        replace_quote(row['PROVINCIA DE RESIDENCIA']),
        replace_quote(row['DISTRITO DE RESIDENCIA']),
        replace_quote(row['LUGAR DE RESIDENCIA']),
        replace_empty(row['TIEMPO DE RESIDENCIA']))
    print query
    conn.execute_non_query(query)
    conn.close()


def get_total_lines():
    with open('../dummy_data/dummy_data0.tsv', 'rU') as csvfile:
        reader = csv.DictReader(csvfile, delimiter="\t")
        i = 0
        for row in reader:
            i += 1
        return i


with open('../dummy_data/dummy_data0.tsv', 'rU') as csvfile:
    reader = csv.DictReader(csvfile, delimiter="\t")
    total = get_total_lines()
    i = 0
    for row in reader:
        importar(row)
        i += 1
        print 'import {0} of {1}'.format(i, total)
