# Clasificador automático de secuencias de imágenes de roedores 🐭

Aplicación utilizada para el proyecto 'Automatic detection of rodent behavior'.

<p align="justify">El objetivo de este proyecto es desplegar la aplicación para que pueda ser accesible por usuarios en remoto. Esta aplicación cuenta con una interfaz sencilla, a la que se envían 24 imágenes y la salida es una clasificación dada por el modelo de Inteligencia Artificial mencionado con anterioridad.</p>

## 🔧 Hito 1: Configuración del repositorio 🔧

<p align="justify">En el siguiente enlace se puede consultar la documentación del <a href="https://github.com/Angburmun/image-sequence-classifier/blob/main/hitos/hito1.md">Hito 1</a>, en el que se detalla cómo se ha creado el repositorio de GitHub para esta aplicación.</p>

## 🕐 Hito 2: Integración continua 🕐

<p align="justify">En el siguiente enlace se puede consultar la documentación del <a href="https://github.com/Angburmun/image-sequence-classifier/blob/main/hitos/hito2.md">Hito 2</a>, en el que se detalla la realización de los tests y la infraestructura virtual de la aplicación.</p>

## 🔬 Hito 3: Diseño de Microservicios 🔬

<p align="justify">En el siguiente enlace se puede consultar la documentación del <a href="https://github.com/Angburmun/image-sequence-classifier/blob/main/hitos/hito3.md">Hito 3</a>, en el que se detalla la separación de la aplicación en microservicios, y se implementa un sistema de <em>logging</em>.</p>

## 📦 Hito 4: Composición de Servicios 📦

<p align="justify">En el siguiente enlace se puede consultar la documentación del <a href="https://github.com/Angburmun/image-sequence-classifier/blob/main/hitos/hito4.md">Hito 4</a>, en el que se detalla cómo se ha descrito la composición de los diferentes contenedores que forman la infraestructura utilizando Docker Compose</p>

## 📂 Disposición de los archivos de la práctica 📂

Aquí debajo viene una explicación de qué son cada uno de los archivos que se encuentran en este repositorio:
   - <p align="justify"><b>README.md</b> es este archivo, con toda la información acerca del repositorio.</p>
   - <p align="justify"><b>LICENSE</b> es la licencia usada para este repositorio. Creative Commons.</p>
   - <p align="justify">Los archivos que comienzan con <b>LSTM</b> y terminados en <b>.h5</b> o <b>.keras</b> son los propios de la red neuronal. Es el clasificador de nuestra aplicación.</p>
   - <p align="justify"><b>.gitignore</b> le dice a <i>git</i> los archivos que no deben estar en el repositorio. Tal y como está explicado en la documentación de la práctica, esto veta archivos binarios o derivados de otros archivos de este repositorio.</p>
   - <p align="justify"><b>app.py</b> tiene todo el código de la aplicación.</p>
   - <p align="justify"><b>test_app.py</b> contiene los tests de la aplicación.</p>
   - <p align="justify">La carpeta <b>templates</b> cuenta con la interfaz html.</p>
   - <p align="justify">La carpeta <b>static</b> tiene la hoja de estilos de la aplicación web.</p>
   - <p align="justify">La carpeta <b>js</b> contiene el FrontEnd de la aplicación.</p>
   - <p align="justify">La carpeta <b>hitos</b> contiene la información de cada uno de los hitos completados para la asignatura Cloud Computing 2024-25. Se puede acceder a esos documentos desde este README, a través de los enlaces individuales que se pueden encontrar en cada uno de los apartados de los hitos individuales.</p>
