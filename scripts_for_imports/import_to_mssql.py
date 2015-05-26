# Copyright 2015 by Vitoko. All rights reserved.
# Revisions 2015 by McPollo. All rights reserved.
# This code is part of the Ventanita distribution and governed by its
# license. Please see the LICENSE file that should have been included
# as part of this package.

import _mssql
import csv


CSV_DATA_FILE = '../dummy_data/dummy_data0.tsv'
DB_SERVER = 's10.winhost.com:1433'
DB_USERNAME = 'DB_76507_ventanita_user'
DB_PASSWORD = '123abc$'
DB_NAME = 'DB_76507_ventanita'


def replace_quote(content):
    if content:
        return content.replace("'", "")


def replace_empty(content):
    if not content:
        return 0


def importar(row):
    conn = _mssql.connect(server=DB_SERVER,
                          user=DB_USERNAME,
                          password=DB_PASSWORD,
                          database=DB_NAME)
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
        replace_quote(row['FECHA DE NACIMIENTO']),
        replace_quote(row['DEPARTAMENTO DE RESIDENCIA']),
        replace_quote(row['PROVINCIA DE RESIDENCIA']),
        replace_quote(row['DISTRITO DE RESIDENCIA']),
        replace_quote(row['LUGAR DE RESIDENCIA']),
        replace_empty(row['TIEMPO DE RESIDENCIA']))
    conn.execute_non_query(query)
    conn.close()


def get_total_lines():
    with open(CSV_DATA_FILE, 'rU') as csvfile:
        return sum(1 for _ in csv.DictReader(csvfile, delimiter="\t"))


with open(CSV_DATA_FILE, 'rU') as csvfile:
    reader = csv.DictReader(csvfile, delimiter="\t")
    total = get_total_lines()
    for i, row in enumerate(reader, 1):
        importar(row)
        print 'import {0} of {1}'.format(i, total)
