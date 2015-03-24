#Esta es ventanita

[![Join the chat at https://gitter.im/aniversarioperu/ventanita](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/aniversarioperu/ventanita?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Poyecto de periodismo de datos con miras a las elecciones presidenciales,
congresales 2016.

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
* python 2.7.5
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

## Licencia
Este es un proyecto *open source* con una licencia permisiva (**WTFPL**, ver archivos
COPYING y LICENSE).
El derecho de autor (*copyright*) en este proyecto corresponde a varias personas.
El *copyright* para cada módulo está indicado al inicio de cada archivo, el cual
corresponde al autor inicial y personas que contribuyeron con adiciones y modificaciones.
