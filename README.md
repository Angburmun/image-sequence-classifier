# Clasificador automático de secuencias de imágenes de roedores

Aplicación utilizada para el proyecto 'Automatic detection of rodent behavior'.

El objetivo de este proyecto es desplegar la aplicación para que pueda ser accesible por usuarios en remoto. Esta aplicación cuenta con una entrada de 24 imágenes y la salida es una clasificación dada por el modelo de Inteligencia Artificial descrito en el proyecto mencionado con anterioridad.


## Hito 1: Configuración del repositorio.

Durante la realización de este hito se ha creado el repositorio de GitHub para la aplicación sobre la que desarrollaremos las prácticas de Cloud Computing. La realización de este proceso no es algo trivial ni ha de darse por hecha, ya que lleva varios pasos como lo son la creación del repositorio, la configuración de la terminal para poder acceder al repositorio, y la adición de los archivos al mismo repositorio.

### Primer paso: *Creacción del repositorio.*
  Para esto debemos crear un repositorio nuevo dentro de nuestra cuenta de GitHub. Hay muchas formas de hacer esto, por ejemplo, se puede crear el repositorio en local y después sincronizarlo con la cuenta de GitHub. Para no complicarnos demasiado, primero voy a crear un repositorio vacío en GitHub, lo clonaré en mi PC y después añadiré los archivos con un commit. En esta immagen se puede ver el proceso:

  ![image](https://github.com/user-attachments/assets/9af3546c-27c9-4d15-ab8c-c6204ad9ede3)

### Segundo paso: *Configurar las claves SSH de nuestro ordenador.*
  Como siguiente paso, para poder conectarnos a nuestro repositorio desde nuestro ordenador, GitHub nos pide que utilicemos claves públicas y privadas para proteger nuestra conexión. Para completar este paso primero tenemos que crear las claves y después tenemos que añadir la clave pública a nuestra cuenta de GitHub. Convenientemente, GitHub tiene un tutorial en el que se explica este proceso muy bien: https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent.

  Algunas capturas de pantalla de esta preparación en mi ordenador:

  ![image](https://github.com/user-attachments/assets/c2371264-a954-423a-9408-fb10cfc8af0c)

  Como buena clave pública, lo único que se puede hacer es darme acceso a un repositorio con ella, por eso la publico aquí ;). También hay que configurar el email y el usuario para poder hacer *commits*. Convenientemente, GitHub te avisa si no están configurados, y se puede hacer con los siguientes comandos:

  ![image](https://github.com/user-attachments/assets/1871d9d1-3251-415c-9c73-a60ea9192130)

  Una vez está todo configurado, podemos pasar al siguiente paso.

  ### Tercer paso: *Subir los archivos*.
  Lo último que nos queda es clonar el repositorio en nuestro ordenador con un *git clone* (con la dirección que aparece en nuestra página del repositorio), copiar los archivos dentro del repositorio y hacer un *git push* con un *git commit* para subir todos los archivos al repositorio:

  ![image](https://github.com/user-attachments/assets/88792f05-dc98-4393-b7dc-9c05e75af0c7)

  ![image](https://github.com/user-attachments/assets/c3fdb4e9-1028-4068-9f1b-2c3102b3d0b4)

  Et voilá! El repositorio está listo y con todos los archivos para estar trabajando. Ahora lo único que queda es redactar este Readme.md (que estoy haciendo ahora mismo, así que esto es una metaescritura). No adjunto capturas de esta parte porque ya se está viendo el resultado :-).
