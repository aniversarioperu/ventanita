[![Build Status](https://travis-ci.org/ventanita/ventanita.svg?branch=master)](https://travis-ci.org/ventanita/ventanita)
[![Coverage Status](https://coveralls.io/repos/ventanita/ventanita/badge.svg)](https://coveralls.io/r/ventanita/ventanita)
[![Stories in Progress](https://badge.waffle.io/ventanita/ventanita.png?label=in progress&title=In Progress)](https://waffle.io/ventanita/ventanita)

[![Throughput Graph](https://graphs.waffle.io/ventanita/ventanita/throughput.svg)](https://waffle.io/ventanita/ventanita/metrics)

#Esta es ventanita

[![Join the chat at https://gitter.im/ventanita/ventanita](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/ventanita/ventanita?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Poyecto de periodismo de datos con miras a las elecciones presidenciales,
congresales 2016.

Ventanita is un proyecto desarrollado por voluntarios. Tus contribuciones y mejoras
al código son bienvenidas.

## Contenido
* [Antecedentes](#antecedentes)

## Antecedentes
En las pasada campaña de Elecciones Regionales y Municipales 2014 ejecutamos el
proyecto **Verita** <http://utero.pe/tag/verita/>.

* Vale la pena hacer algo similar?
* Algo mejor?

Necesitamos ideas. Aporte y discusión de ideas aquí:
<https://github.com/aniversarioperu/ventanita/issues>

## Objetivo principal
Hacer un *aplicativo* web usando el **framework Django**. Este aplicativo permitirá 
que usuarios puedan dar evaluar rápidamente la idoneidad de los candidatos y
partidos políticos que se presenten a las Elecciones 2016.

Idealmente algo parecido al aplicativo uterino <http://www.selallevanfacil.info/home/>.


## Dependencias
* python3
* ``pip install -r requirements/testing.txt``

## Configuración
Puedes poner tus datos de desarrollo local en un archivo ``config.json``,
asegurándote que haya sido incluido en tu ``.gitignore``.

```javascript
{
    "SECRET_KEY": "crear una clave secreta",
    "DB_USER": "usuario de base de datos postgreSQL",
    "DB_PASS": "tu contraseña para la base de datos",
    "DB_NAME": "ventanita",
    "DB_PORT": "5432",
    "DB_HOST": "localhost"
}
```

## Ejecutar la aplicación
Puede usar el ``Makefile`` de ventanita:

```shell
> make serve
```

## Scripts para importar datos
Van en el folder ``scripts_for_imports``:

* Puedes importar el ``dummy_data`` a una base de datos MSSQL usando el script
  ``import_to_mssql.py``.
* Importar registros del REDAM: 
  ``python ventanita/manage.py import_redam --jsonfile=redam.jl --settings=ventanita.settings.local``
* Importar hojas_de_vida: 
  ``python ventanita/manage.py import_hojas_de_vida --tsvfile=dummy_data0.tsv --settings=ventanita.settings.local``
  

## Licencia
Este es un proyecto *open source* con una licencia permisiva (**WTFPL**, ver archivos
COPYING y LICENSE).
El derecho de autor (*copyright*) en este proyecto corresponde a varias personas.
El *copyright* para cada módulo está indicado al inicio de cada archivo, el cual
corresponde al autor inicial y personas que contribuyeron con adiciones y modificaciones.
