# 📦 Hito 4: Composición de Servicios 📦

<p align="justify">A lo largo de este hito se describirá cómo desacoplar una aplicación monolítica en diferentes servicios para desplegarla en la nube en futuros hitos. También se describirán las prácticas que se han seguido al orquestrar los servicios con Docker, y buenas prácticas en general a seguir cuando estemos desarrollando los servicios de nuestra aplicación.</p>

## Desacoplando la aplicación
<p align="justify">Para poder convertir la aplicación a diferentes servicios, primero tenemos que desacoplar las diferentes funcionalidades que tiene nuestra aplicación. Un buen ejemplo de cómo realizar esto sería separar la lógica de negocio, de la base de datos y del frontend. En mi caso particular, decidí separar la aplicación en tres servicios: la aplicación, logs y tests - sin una base de datos porque no tendría sentido su inclusión.</p>

### Aplicación y logging
<p align="justify">Para desacoplar la aplicación, primero se tuvo que detallar la dirección IP y el puerto dados a Flask. Desconozco la razón, pero no funcionaba si no se especificaba que el servidor debía de lanzarse a la dirección 0.0.0.0:5000. El mayor cambio que ha tenido el archivo <code>app.py</code> es el cambio de <em>loigging</em> de <em>Python</em> por el uso de la librería <code>fluentd</code>. Esta librería envía los logs a otro servidor, que los recibe en el puerto UDP 24224 y los escribe en un archivo. PD: Importante crear un <code>fluent.conf</code> para <code>fluentd</code>, de lo contrario, no funcionará.</p>

![image](https://github.com/user-attachments/assets/b6ac7165-83d6-4da9-b144-2e4228a83122)

<p align="justify">El principal beneficio de usar esta herramienta es que ya no estamos restringidos a únicamente la aplicación para guardar logs, sino que también podemos hacer que nuestros tests manden peticiones para guardarlo, o, quién sabe, incluso futuras expansiones y servicios que se añadan también podrían aprovechar este contenedor para realizar logging.</p>

### Tests

<p align="justify">Desacoplar los tests ha sido más difícil que desacoplar los logs de la aplicación Flask. Los tests estaban programados para que se lanzara la aplicación en local, y se realizaran las pruebas sobre esa instancia, sin conectarse realmente a una aplicación desplegada. Para esto, se ha tenido que utilizar la librería <code>requests</code>, para realizar peticiones al servidor lanzado en nuestra orquestración.</p>

![image](https://github.com/user-attachments/assets/bdf20f1c-3c60-465a-88f3-ef59f30f2b33)

## Orquestración de servicios
<p align="justify">Una vez están desacopladas las aplicaciones, podemos utilizar Docker para coordinar todos nuestros servicios. Creamos tantos Dockerfiles como necesitemos - en nuestro caso, uno por contenedor, donde especificaremos las características de los contenedores que lanzaremos. Realmente no tenemos por qué desacoplar primero la aplicación y después orquestrar los servicios, sino que podemos trabajar para realizar un desacople escalonado. Por ejemplo, en mi caso, yo trabajé de la siguiente forma: primero comprobé que mi aplicación monolítica funcionara en un único contenedor (ahí descubrí ciertos problemas con Flask). Después he ido desacoplando los tests primero, y despues los logs. Por último, he ajustado GitHub Actions para que funcione con la versión desacoplada de la aplicación, pero hablaré de eso un poco más tarde.</p>

### Dockerfiles
<p align="justify">Podemos visitar los diferentes Dockerfiles en la carpeta raíz del proyecto. Para App y Tests se ha partido de una imagen <code>Python:3.9-slim</code> a la que se le han instalado los requerimientos justos, y se han copiado los archivos justos para que funcione lo necesario. En el caso de los Logs, <code>fluentd</code> tiene disponible una imagen de Docker con todo lo necesario para trabajar sin instalar ninguna cosa extra. También se ha especificado la versión de la imagen para que, si en un futuro aparecen actualizaciones para alguna de estas aplicaciones, no tengamos problemas de compatibilidad y se descarguen versiones con las que ya se ha comprobado que todo funciona.</p>

![image](https://github.com/user-attachments/assets/49249f02-3186-4f21-8b16-841befc69fa1)

<p align="justify">Mediante un docker-compose.yml podemos describir los diferentes servicios que componen nuestra orquestración, creando redes entre ellos y definiendo dependencias y volúmenes de datos. La implementación se puede consultar en el archivo <a href="https://github.com/Angburmun/image-sequence-classifier/blob/main/docker-compose.yaml">docker-compose.yaml</a> en la raíz del repositorio. En resumen, existen tres servicios: Logs > App > Tests, que se despliegan en ese orden. Se utiliza una red virtual interna para conectar a los tres servicios, y el contenedor de Logs tiene un volumen para guardar sus datos de manera persistente.</p>

![image](https://github.com/user-attachments/assets/5a1daf37-504a-4d44-b5c0-cdda2221825e)

## Actualizando GitHub Actions
<p align="justify">Una vez comprobemos que todos nuestros servicios funcionan, es hora de actualizar los flujos de trabajo de GitHub Actions para que reflejen las pruebas con nuestros servicios desacoplados. Para ponerlo a funcionar instalamos <code>docker-compose</code> en el contenedor base, desde el que lanzaremos los diferentes servicios. En un primer paso lanzamos App - que a su vez lanzará Logs porque depende de él, y después lanzamos Tests para comprobar que todo funciona correctamente. La implementación de los flujos de trabajo también se pueden comprobar en el <a href="https://github.com/Angburmun/image-sequence-classifier/blob/main/.github/workflows/docker-publish.yml">docker-publish.yml</a> dentro de la carpeta <code>.github/workflows/</code></p>

![image](https://github.com/user-attachments/assets/ff6cbde7-9cce-44dd-ab4f-d3cbe14b9eaf)

<p align="justify">Y con esto terminaríamos este Hito. ¡Ahora mismo en el repositorio tenemos todo listo para generar nuestras imágenes de Docker para desplegar nuestro servicio!</p>
