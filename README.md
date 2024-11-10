# Clasificador automático de secuencias de imágenes de roedores

Aplicación utilizada para el proyecto 'Automatic detection of rodent behavior'.

<p align="justify">El objetivo de este proyecto es desplegar la aplicación para que pueda ser accesible por usuarios en remoto. Esta aplicación cuenta con una entrada de 24 imágenes y la salida es una clasificación dada por el modelo de Inteligencia Artificial descrito en el proyecto mencionado con anterioridad.</p>

  ### Disposición de los archivos de la práctica.

  Ya que estamos, aquí debajo viene una explicación de qué son cada uno de los archivos que se encuentran en este repositorio:
   - **README.md** es este archivo, con toda la información acerca del repositorio.
   - **LICENSE** es la licencia usada para este repositorio. Creative Commons, porque la he utilizado con anterioridad y satisface todas las necesidades para este trabajo.
   - Los archivos que comienzan con **LSTM** y terminados en **.h5** o **.keras** son los propios de la red neuronal. Es el clasificador de nuestra aplicación.
   - **.gitignore** le dice a *git* los archivos que no deben estar en el repositorio. Tal y como está explicado en la documentación de la práctica, esto veta archivos binarios o derivados de otros archivos de este repositorio.
   - **app.py** tiene todo el código de la aplicación.
   - La carpeta **templates** tiene el FrontEnd de la aplicación, en este caso una aplicación web.
   - La carpeta **static** tiene la hoja de estilos de la aplicación web.
