CREATE TABLE Candidatos(
    DNI NVARCHAR(10) NOT NULL,
    DEPARTAMENTO_AL_QUE_POSTULA NVARCHAR(500),
    PROVINCIA_AL_QUE_POSTULA NVARCHAR(500),
    DISTRITO_AL_QUE_POSTULA NVARCHAR(500),
    ID_CANDIDATO INT,
    ORGANIZACION_POLITICA	NVARCHAR(500),
    CARGO_AL_QUE_POSTULA NVARCHAR(500),
    DESIGNACION NVARCHAR(500),
    APELLIDO_PATERNO NVARCHAR(500),
    APELLIDO_MATERNO NVARCHAR(500),
    NOMBRE_COMPLETO NVARCHAR(500),
    SEXO NVARCHAR(10),
    CORREO_ELECTRONICO NVARCHAR(500),
    DEPARTAMENTO_DE_NACIMIENTO NVARCHAR(500),	
    PROVINCIA_DE_NACIMIENTO NVARCHAR(500),
    DISTRITO_DE_NACIMIENTO NVARCHAR(500),
    FECHA_DE_NACIMIENTO NVARCHAR(500),
    DEPARTAMENTO_DE_RESIDENCIA NVARCHAR(500),
    PROVINCIA_DE_RESIDENCIA NVARCHAR(500),
    DISTRITO_DE_RESIDENCIA NVARCHAR(500),
    LUGAR_DE_RESIDENCIA NVARCHAR(500),
    TIEMPO_DE_RESIDENCIA INT
)