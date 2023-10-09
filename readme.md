# Bienvenido al Proyecto de Blog en Django y Python

Este proyecto se trata de una página web construida con Django y Python que te permite crear y compartir ideas a través de publicaciones. Con esta aplicación web, los usuarios pueden registrarse, iniciar sesión, comenzar a crear sus propias publicaciones, editarlas y cerrar sesión.

---

### Secciones:

- La aplicación web se escuentra divida en las secciones: Home, Acerca de mi, Blog y Perfil.
- En la sección Acerca de mí, se puede leer un breve comentario del autor.
- Cuenta con la posibilidad de registrarse, iniciar sesión y editar la información del usuario, como email, nombre, apellido,como también la posibilidad de cambiar su contraseña.
- En la sección Blog, cada usuario puede ver las distintas publicaciones, como también crearlas, colocar una imagen y editarlas, solo las que el usuario creó.

---

### Configuración y Uso:

- Clona este repositorio en tu máquina local.

- Instala las dependencias del proyecto.

- Ejecuta las migraciones de la base de datos con el comando

```python
python manage.py migrate.
```

- Crea un superusuario administrativo con el siguiente comando. Esto te permitirá administrar fácilmente la plataforma.

```python
python manage.py createsuperuser
```

- Inicia el servidor de desarrollo con el siguiente comando y accede a la aplicación en tu navegador.

```python
python manage.py runserver
```
