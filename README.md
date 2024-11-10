# Clasificador automático de secuencias de imágenes de roedores

Aplicación utilizada para el proyecto 'Automatic detection of rodent behavior'.

<p align="justify">El objetivo de este proyecto es desplegar la aplicación para que pueda ser accesible por usuarios en remoto. Esta aplicación cuenta con una entrada de 24 imágenes y la salida es una clasificación dada por el modelo de Inteligencia Artificial descrito en el proyecto mencionado con anterioridad.</p>


## Hito 1: Configuración del repositorio.

<p align="justify">Durante la realización de este hito se ha creado el repositorio de GitHub para la aplicación sobre la que desarrollaremos las prácticas de Cloud Computing. La realización de este proceso no es algo trivial ni ha de darse por hecha, ya que lleva varios pasos como lo son la creación del repositorio, la configuración de la terminal para poder acceder al repositorio, y la adición de los archivos al mismo repositorio.</p>

### Primer paso: *Creacción del repositorio.*
  <p align="justify">Para esto debemos crear un repositorio nuevo dentro de nuestra cuenta de GitHub. Hay muchas formas de hacer esto, por ejemplo, se puede crear el repositorio en local y después sincronizarlo con la cuenta de GitHub. Para no complicarnos demasiado, primero voy a crear un repositorio vacío en GitHub, lo clonaré en mi PC y después añadiré los archivos con un commit. En esta immagen se puede ver el proceso:</p>

  ![image](https://github.com/user-attachments/assets/9af3546c-27c9-4d15-ab8c-c6204ad9ede3)

### Segundo paso: *Configurar las claves SSH de nuestro ordenador.*
  <p align="justify">Como siguiente paso, para poder conectarnos a nuestro repositorio desde nuestro ordenador, GitHub nos pide que utilicemos claves públicas y privadas para proteger nuestra conexión. Para completar este paso primero tenemos que crear las claves y después tenemos que añadir la clave pública a nuestra cuenta de GitHub. Convenientemente, GitHub tiene un tutorial en el que se explica este proceso muy bien: https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent.</p>

  Algunas capturas de pantalla de esta preparación en mi ordenador:

  ![image](https://github.com/user-attachments/assets/c2371264-a954-423a-9408-fb10cfc8af0c)

  <p align="justify">Como buena clave pública, lo único que se puede hacer es darme acceso a un repositorio con ella, por eso la publico aquí ;). También hay que configurar el email y el usuario para poder hacer *commits*. Convenientemente, GitHub te avisa si no están configurados, y se puede hacer con los siguientes comandos:</p>

  ![image](https://github.com/user-attachments/assets/1871d9d1-3251-415c-9c73-a60ea9192130)

  Una vez está todo configurado, podemos pasar al siguiente paso.

  ### Tercer paso: *Subir los archivos*.
  <p align="justify">Lo último que nos queda es clonar el repositorio en nuestro ordenador con un *git clone* (con la dirección que aparece en nuestra página del repositorio), copiar los archivos dentro del repositorio y hacer un *git push* con un *git commit* para subir todos los archivos al repositorio:</p>

  ![image](https://github.com/user-attachments/assets/88792f05-dc98-4393-b7dc-9c05e75af0c7)

  ![image](https://github.com/user-attachments/assets/c3fdb4e9-1028-4068-9f1b-2c3102b3d0b4)

  <p align="justify">Et voilá! El repositorio está listo y con todos los archivos para estar trabajando. Ahora lo único que queda es redactar este Readme.md (que estoy haciendo ahora mismo, así que esto es una metaescritura). No adjunto capturas de esta parte porque ya se está viendo el resultado :-).</p>

  ### Disposición de los archivos de la práctica.

  Ya que estamos, aquí debajo viene una explicación de qué son cada uno de los archivos que se encuentran en este repositorio:
   - **README.md** es este archivo, con toda la información acerca del repositorio.
   - **LICENSE** es la licencia usada para este repositorio. Creative Commons, porque la he utilizado con anterioridad y satisface todas las necesidades para este trabajo.
   - Los archivos que comienzan con **LSTM** y terminados en **.h5** o **.keras** son los propios de la red neuronal. Es el clasificador de nuestra aplicación.
   - **.gitignore** le dice a *git* los archivos que no deben estar en el repositorio. Tal y como está explicado en la documentación de la práctica, esto veta archivos binarios o derivados de otros archivos de este repositorio.
   - **app.py** tiene todo el código de la aplicación.
   - La carpeta **templates** tiene el FrontEnd de la aplicación, en este caso una aplicación web.
   - La carpeta **static** tiene la hoja de estilos de la aplicación web.
