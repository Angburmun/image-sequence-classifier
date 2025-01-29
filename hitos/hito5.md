# 🚀 Hito 5: Despliegue de la aplicación en un PaaS 🚀

<p align="justify">En este hito se describen los pasos a seguir para desplegar nuestra aplicación <em>Dockerizada</em> en un PaaS, o Platform as a Service. Durante esta práctica se explicarán los problemas surgidos a la hora de encontrar una plataforma, y en el momento de ejecutar nuestra orquestación en la nube - ya que no todas las plataformas ofrecen compatibilidad con <code>docker-compose</code>.</p>

## Variables de entorno
<p align="justify">El primer paso para poder desplegar nuestra aplicación en un PaaS correctamente es la de crear variables de entorno para hacer nuestra orquestación más flexible. Las variables de entorno son variables del código que podemos modificar antes de ejecutarlo desde el sistema en el que ejecutemos los contenedores. Por ejemplo, las direcciones y puertos de los contenedores de App y Logs, para conectarlos entre sí.</p>

![image](https://github.com/user-attachments/assets/7bdacefd-cbcb-4475-8dd1-f35b32f04679)

<p align="justify">Podemos marcar las variables en nuestro <a href="https://github.com/Angburmun/image-sequence-classifier/blob/main/docker-compose.yaml">docker-compose.yaml</a>, y referenciarlas en un archivo <code>.env</code>. Desde este archivo podemos establecer los valores que queremos para nuestra aplicación. En mi caso estoy utilizando las direcciones internas de la red virtual creada por Docker.</p>

![image](https://github.com/user-attachments/assets/426daa4e-2ed6-4138-9118-6495b95fdcac)

## Render
<p align="justify">Al tener nuestras variables de entorno separadas del código, podemos utilizar un PaaS como <a href="https://render.com/">Render</a> para desplegar nuestro servicio. Por desgracia, Render no soporta docker-compose directamente, pero sí que soporta imágenes de Docker, así que podemos subir nuestras imágenes a Docker.io para que sean accesibles desde Render. O también podemos cargar directamente nuestro repositorio de GitHub, y trabajar con los Dockerfile que hemos creado en hitos anteriores.</p>

![image](https://github.com/user-attachments/assets/83098ece-a12e-4ec8-8dd7-86437d63082d)

<p align="justify">Gracias a haber separado las variables de entorno de nuestro código, ahora podemos introducirlas de una en una en los contenedores en los que las necesitamos para que los contenedores se conecten correctamente. Plataformas como AWS permiten el uso directamente de docker-compose, lo cual ayuda con la seguridad y elimina posibles fallos - pero esto es con lo que podemos trabajar si queremos hacerlo de manera gratuita.</p>

![image](https://github.com/user-attachments/assets/340e2cbb-4f9f-4861-b7af-1fb6cccddb1b)

## EXTRA: Imágenes de Docker
<p align="justify">Si queremos utilizar imágenes de Docker en vez de cargar la información desde el repositorio de GitHub, podemos utilizar las imágenes que estamos creando en local. Al ejecutar <code>docker-compose up --build</code>, estamos creando una imagen de Docker por cada servicio que lanzamos. Si renombramos estas imágenes correctamente a <code>usuario/nombre:etiqueta</code>, podemos subirlas a Docker hub, y hacerlas públicas para poder descargarlas. <a href="https://docs.docker.com/">Docker docs</a> tiene un tutorial muy bueno acerca de cómo llevar a cabo estos pasos.</p>

![image](https://github.com/user-attachments/assets/f06fef09-206e-4a7b-864f-9e7d78d07d87)

<p align="justify">Y después de haber explicado esto, tenemos nuestro servicio funcionando en el enlace <a href="https://flask-app-rip6.onrender.com:5000">imgae-sequence-classifier</a>. Con esto se dan por terminadas las prácticas de esta asignatura.</p>
