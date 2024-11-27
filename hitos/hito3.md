# 🔬 Hito 3: Diseño de Microservicios 🔬

<p align="justify">Durante el desarrollo de este hito se separará la lógica de la aplicación para que sea accesible a través de una API <em>REST</em> y se añadirá un sistema de <em>logs</em> para saber lo que está ocurriendo en el sistema en cada momento.</p>

## Diseñando la API <em>REST</em>
<p align="justify">El hecho de que nuestra aplicación sea accesible a través de una API es muy importante, ya que nos ayuda a que nuestro proyecto sea escalable, fiable y fácilmente depurable. Desacoplando la lógica en diferentes microservicios podemos acceder a cada uno de ellos de manera individual; modificarlos, actualizarlos o incluso eliminarlos no debería afectar al resto del funcionamiento de la aplicación (a no ser que existan dependencias).</p>
<p align="justify">Por suerte, este proyecto ya se desarrolló con una API <em>REST</em> como eje central desde el comienzo del desarrollo. Los detalles de la API se pueden ver dentro del propio <em><a href="https://github.com/Angburmun/image-sequence-classifier/blob/main/app.py">app.py</a></em>, donde encontramos de primera mano los <em>endpoints</em> que hay abiertos. Las solicitudes <em>POST</em> que realiza el <em>frontend</em> también se pueden visitar en el archivo <em><a href="https://github.com/Angburmun/image-sequence-classifier/blob/main/static/script.js">script.js</a></em>.</p>

![image](https://github.com/user-attachments/assets/38e83312-746c-4513-ae60-90239e14d919)

## Registrando las llamadas del sistema
<p align="justify">Otro punto importante de este hito es el de desarrollar un sistema efectivo de registro o <em>logging</em>. Con este sistema se pretende mantener en un archivo todo lo que sucede en nuestra aplicación; desde llamadas a los endpoints hasta las respuestas que se dan, incluyendo errores, fallos críticos y otros accesos. Los mensajes de registro y la implementación se encuentran en el archivo <em><a href="https://github.com/Angburmun/image-sequence-classifier/blob/main/app.py">app.py</a></em>, después de cada uno de los eventos que modifican el estado del sistema.</p>

![image](https://github.com/user-attachments/assets/cf392e66-e8e1-4f1e-9c5f-1d4681061b99)

<p align="justify">En esta implementación se ha decidido utilizar la librería estándar <em>logging</em> de <em>python</em>, por contra de los <em>logs</em> que nos proporciona la librería <em>flask</em>. En realidad no es importante cual de las dos utilizar, pero si quisiéramos expandir el sistema con funcionalidad que no es dada por <em>flask</em>, es posible que tuviéramos más problemas para registrar la información existente que con la librería genérica de <em>python</em>.</p>

<p align="justify">Gracias a las prácticas de programación que hemos aprendido a lo largo de nuestra vida académica, nos hemos ahorrado trabajo durante el desarrollo de este hito. Explicada la API y el sistema de <em>logging</em>, hemos terminado esta parte.</p>
