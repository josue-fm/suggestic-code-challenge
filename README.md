# Indicaciones generales
Para poder ejecutar la aplicación en docker se deben seguir los pasos que se mencionan a continuación.

## 1. Construir la imagen de docker para la app
Para construir la imagen se puede realizar ejecutando un comando como el del siguiente ejemplo:
```
docker build -t my-image .
```
Se debe de ejecutar en el directorio donde se encuentre el archivo `Dockerfile`.

## 2. Ejecutar el contenedor
La aplicación hace uso de mongo db para guardar los resultados del servicio.
Para ejecutar el contenedor es necesario pasar las siguientes variables de entorno:
- __DB_HOST__: Host de la base de datos (_requerida_)
- __DB_PORT__: Puerto de la base de datos (_requerida_)
- __DB_USR__: Usuario de la base de datos (_opcional_)
- __DB_PSW__: Contraseña de la baser de datos (_opcional_)

Para ejecutar el contenedor se puede realizar mediante un comando como el siguiente ejemplo:
```
docker run -p 8080:80 \
-e DB_HOST=my-mong-db.com \
-e DB_PORT=27017 \
--name my-app my-image
```

La aplicación se puede conectar a una base de datos de mongo db que no requiera autenticación y también a una que permita la autenticación por default.


## Notas finales
- La aplicación usa el framework `FastAPI` y `unvicorn como servidor web.
- Una vez que el servicio este corriendo correctamente, se puede revisar el path `/docs` para ver la documentación del servicio. Por ejemplo si el servicio esta corriendo de forma local y accesible a través del puerto `8080`, podemos acceder a la url http://localhost:8080/docs
