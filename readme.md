# Ingeniería de Software

Evaluación Final Integradora 2024 Parte I

Integrantes:

de Rivas, Pablo

Profesor:

Lucero, Matias Javier

## Descripción del Proyecto

Sistema web para una concesionaria desarrollado con Django. Cuenta con sección de listado, busqueda, detalles y ventas de autos.

## Instalación

1. Clonaremos el repositorio ``` git clone git@github.com:PDeRivas/efi_ing_software_1.git ``` e ingresamos a su carpeta `` cd efi_ing_software_1 ```
2. Crearemos un entorno virtual ``` python3 -m venv venv ``` y lo corremos ``` source venv/bin/activate ```
3. Instalaremos las librerias utilizadas ``` pip install -r requirements.txt ```

## Correr la aplicación

1. Cuando nos encontremos en la carpeta principal del proyecto entraremos al directorio concesionaria ``` cd concesionaria ```
2. Correremos las migraciones ``` python3 manage.py makemigrations ``` ``` python3 manage.py migrate ```
3. Iniciaremos el proyecto ``` python3 manage.py runserver ```
4. Ir al navegador y entrar a [127.0.0.1:8000](http://127.0.0.1:8000/)

## Comandos

Aparte de correr el proyecto tendremos acceso al comando cargar_datos, y le pasaremos como argumento vehiculos.csv ``` python3 manage.py cargar_datos vehiculos.csv ```. Este carga todos los vehiculos dentro del archivo, tambien creando todos los modelos asociados (Marcas, Categorias, Thumbnails, etc). Consigue imagenes de la carpeta cars_images para poner de thumbnail.

Tambien podemos usar el comando borrar_autos ``` python3 manage.py borrar_autos ```. Este borra todos los autos cargados, pero no los otros modelos.

## Rutas de la API

<details>
  <summary>1. GET http://127.0.0.1:8000/api/cars/ Para obtener un listado completo de todos los autos creados en la base de datos.</summary>
  
   ### Devuelve los siguientes elementos de cada auto:
  
   id
   
   Year (año)
   
   Brand (marca) anidado del modelo marca.
   
   Category (categoría) anidado del modelo categoría.
   
   Country (país) anidado del modelo país.
   
   Fuel (combustible) anidado del modelo combustible.
   
   Nameplate (modelo) anidado del modelo "Modelo" (El nombre nameplate no significa exactamente modelo, pero usar el nombre Model crea problemas con la clase Model de Django).
   
   Traction (tracción) anidado del modelo tracción.
   
   Transmission (transmisión) anidado del modelo transmisión.
   
   Used (usado).
   
   Km (kilometros).
   
   Cylinders (cilindrado).
   
   Price (precio).
   
   Sold (vendido).
</details>

2. GET http://127.0.0.1:8000/api/brands/ Devuelve un listado de todas las marcas.

3. GET http://127.0.0.1:8000/api/category/ Devuelve un listado de todas las categorias.

4. GET http://127.0.0.1:8000/api/nameplates/ Devuelve un listado de todos los modelos de autos.

5. GET http://127.0.0.1:8000/api/fuel/ Devuelve un listado de todos los tipos de combustible.

6. GET http://127.0.0.1:8000/api/traction/ Devuelve un listado de todos los tipos de tracción.

7. GET http://127.0.0.1:8000/api/transmission/ Devuelve un listado de todos los tipos de transmisión.

<details>

<summary>8. POST http://127.0.0.1:8000/api/login_api/ Para recibir el token de usuario para usar desde un administrador de API externo.</summary>

  Necesitamos enviar los siguientes datos:
  
  "username" Nombre de usuario

  "password" Contraseña

  Nos devuelve un token, para usarlo en los sitios que necesite autenticación enviaremos:

  Header ``` Authorization ``` valor ``` Token [nuestro token] ```
</details>
  
<details>

<summary>9. GET http://127.0.0.1:8000/api/users/ Devuelve un listado de todos los usuarios.</summary>

Necesitamos habernos logeado en la sesión actual en el navegador o enviar el Token de usuario en la API. Tambien podemos crear usuarios mediante el método POST:

  1. "username" Nombre del usuario a crear. No puede repetirse con uno ya existente.
  
  2. "password": Contraseña del nuevo usuario.
  
  3. "first_name" Nombre

  4. "last_name" Apellido

  5. "email" Mail del nuevo usuario. Tampoco puede repetirse. 
</details>

## Usuarios

1. No logueado: Puede ver el listado de autos, filtrar y ver detalles, pero no dejar comentarios ni reseñas.
2. Usuario no staff: Puede dejar comentarios y reseñas. Tambien puede editarlos y borrarlos siempre y cuando sea el creador. Para crear uno debemos entrar a iniciar sesión en la navbar del sitio y hacer click en "¿No tenes cuenta? Registrate aqui"
3. Usuario staff: Puede cargar autos, imagenes, marcas, etc desde la sección para administradores [127.0.0.1:8000/admin](http://127.0.0.1:8000/admin). Tambien puede borrar comentarios y reseñas de otros usuarios. Para crear un usuario staff debemos correr el comando ``` python3 manage.py createsuperuser ``` por consola y llenar los campos que nos solicita.

## Admin

Entrando a ``` 127.0.0.1:8000/admin ``` tendremos acceso a las opciones para agregar nuevos autos, marcas, paises, imagenes de autos entre otras cosas.

## Modelos

El principal modelo es el de Auto (Car), y tambien tenemos tambien sus clases foraneas: Marca, Categoría, País, Tipo de Combustible, Modelo, Tipo de tracción y de Transmisión.

CarImage: Imagenes que se utilzian para la galería en el detalle del auto, distinta a la imagen 'Thumbnail' que posee Auto en si y es la que aparece en las tarjetas del Listado de autos.

Comment: Comentarios que pueden realizarse sobre los autos. Pueden ingresarse cualquier cantidad por auto y solo su creador puede editarlos. Un usuario Staff y el Creador pueden borrarlos.

Review: Solo habrá una reseña por usuario. Aqui debe ingresarse un texto y una puntuación que ira del 1 al 10. Posee los mismos permisos de creación y edición que un comentario.

Sale: Ventas realizadas. Guarda todos los datos del usuario que realizo la compra y del auto que se vendio.

## Filtrado

En la template del listado de autos tendremos acceso a un filtro de autos segun precio, categoria, marca, año del auto y si es usado o nuevo.

## Listado de ventas

Los usuarios staff tienen acceso a una lista con datos de todas las ventas de autos realizadas.

## Formularios

Se utilizan formularios localizados en archivos ``` form.py ``` para la creación de todos los formularios de la aplicación, estos son para:
* Login de usuario
* Registro de usuario
* Creación y edición de comentarios
* Creación y edición de reseñas
* Filtrado de autos
* Compra de autos
