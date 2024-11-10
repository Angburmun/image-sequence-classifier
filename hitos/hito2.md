# Hito 2: Integración Continua.

<p align="justify">En este hito se propone crear los tests que comprobarán el correcto funcionamiento de nuestra aplicación, además de su incorporación en una plataforma de integración continua como es GitHub Actions.</p>

## Elección de la librería de tests
<p align="justify">Como primer paso para desarrollar esta práctica, debemos elegir una librería de testing que funcione con el lenguaje de programación de nuestra aplicación. En mi caso, al estar utilizando <em>Python</em>, he decidido utilizar la librería <em>Pytest</em> - también por recomendación de la profesora.</p>
<p align="justify">La documentación de esta librería se puede consultar en el enlace <em><a href="https://docs.pytest.org/">pytest documentation</a></em>.</p>

## Desarrollo de los tests
<p align="justify">Siguiendo las buenas prácticas de programación que se nos han enseñado a lo largo del Grado en Ingeniería Informática, hay varias cosas a tener en cuenta al diseñar tests para nuestra aplicación. Aparte de las técnicas de programación limpia, que ya las damos por supuestas, es importante realizar pruebas de todos los aspectos posibles de nuestra aplicación. Esto nos permitirá tener plena confianza en que el código está funcionando correctamente.</p>

<p align="justify">Recordemos el funcionamiento de la aplicación. Toma una secuencia de 24 imágenes y debe devolver una clasificación para esa secuencia. En caso de no recibir el número adecuado, debe devolver un error. Los detalles de la implementación se pueden ver en el archivo <em><a href="https://github.com/Angburmun/image-sequence-classifier/blob/main/app.py">app.py</a></em>. Las pruebas que tienen sentido, entonces para nuestra aplicación son las siguientes:</p>

<ul>
  <li>Archivos estáticos</li>
  <li>Ruta principal e <em>index.html</em></li>
  <li>Predicción de imágenes</li>
  <ul>
    <li>Ninguna imagen</li>
    <li>Pocas imágenes</li>
    <li>Demasiadas imágenes</li>
    <li>Imágenes corruptas</li>
    <li>Imágenes demasiado grandes</li>
    <li>Imágenes demasiado pequeñas</li>
  </ul>
</ul>

<p align="justify">Los detalles de qué tests se han implementado y cómo se han implementado se pueden ver en el archivo <em><a href="https://github.com/Angburmun/image-sequence-classifier/blob/main/test_app.py">test_app.py</a></em>. Básicamente <em>pytest</em> crea un pequeño entorno con la aplicación, y prueba de forma independiente los diferentes parámetros que le pedimos. El resultado de la ejecución en local es el siguiente:</p>

![image](https://github.com/user-attachments/assets/e5897579-c667-40b4-a282-d683070b7969)

## Integración continua
<p align="justify">Una vez nos hemos asegurado de que todo funciona correctamente en local, es hora de actualizar nuestro repositorio y configurar el entorno de integración continua. En mi caso he decidido utilizar GitHub Actions porque es muy fácilmente integrable con nuestro repositorio de GitHub. Además de que también contiene muchos entornos <em>Python</em> por defecto que podemos utilizar directamente <em>out of the box</em> con pocos cambios.</p>

![image](https://github.com/user-attachments/assets/1f1b0138-7cb7-41ad-9871-3c83825d1bad)

<p align="justify">En mi caso he uno de los contenedores que había para tenerlo de plantilla, junto con el ejemplo existente en la <em><a href="https://docs.github.com/es/actions/writing-workflows/quickstart">Guía de Inicio Rápido de GitHub Actions</a></em>, para escribir mi contenedor. Una vez hecho esto, y tras entender cómo funcionan los archivos yml, ya se pueden escribir los comandos que queremos que se ejecuten en nuestro contenedor. Se dividen en dos partes principales: las dependencias y el comando para pasar los tests. Ambas partes se pueden ver en la captura incluida aquí debajo, o, en su defecto, en el archivo <em><a href="https://github.com/Angburmun/image-sequence-classifier/blob/main/.github/workflows/python-publish.yml">python-publish.yml</a></em>.</p>

![image](https://github.com/user-attachments/assets/9c36c59f-1a54-4836-8347-9f9804d8615b)

<p align="justify">Dentro de este archivo, descubriremos que nuestro repositorio de GitHub se copia automáticamente a nuestro contenedor si ejecutamos el comando <code>ls -la</code>. El resultado de la ejecución se puede ver aquí debajo.</p>

![image](https://github.com/user-attachments/assets/48eab5cc-e370-421b-bd15-82421a69dce3)

<p align="justify">Y después de haber realizado esto, cada vez que realicemos un push se ejecutará nuestro contenedor y pasará todos los tests que tenemos dentro de <em><a href="https://github.com/Angburmun/image-sequence-classifier/blob/main/test_app.py">test_app.py</a></em>. Con esto y un bizcocho, hemos terminado el segundo hito.</p>
