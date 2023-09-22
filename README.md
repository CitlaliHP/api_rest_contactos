# Documento de diseño: API REST CONTACTOS
1.Descripción Ejemplo de una API REST para gestionar contactos en una BD utilizando FASTAPI.

## 2.- Objetivo 
Realizar un ejemplo de diseño de una API REST de tipo CRUD y su posterior codificación utilizando el framwork (FASTAPI) ( https://fastapi.tiangolo.com/ ).

## 3.- Diseño de la bd
Para este ejem´plo se utilizará el gestor de base de datos (SQLITE3) ( https://www.sqlite.org/index.html ) con las siguientes tablas:

## 3.1 Tabla: contactos
|No.|Campo|Tipo|Restricciones|Descripción|
|--|--|--|--|--|
|1|id_contactos|int|PRIMARY KEY|Llave primaria de la tabla|
