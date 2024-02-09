# Práctica 1 - UDP
## Introducción
En esta práctica se ha desarrollado en Python un módulo para la implementación de un juego online mediante mensajes UDP. Este juego consiste en un sistema de preguntas y respuestas (estilo trivial). Para la obtención de las preguntas y respuestas, se empleará la API https://the-trivia-api.com/. Todo el código del juego se encuentra dentro de la carpeta **Entregable**
## Explicación del código
1. **Comunicaciones con la API (API.py)**
    - `get_pregunta_aleatoria()`: Esta función se encarga de obtener una pregunta aleatoria de la API externa. Primero elige aleatoriamente una pregunta del diccionario de preguntas disponibles, luego extrae la información relacionada a esa pregunta (posibles respuestas y respuesta correcta), y finalmente devuelve un diccionario con la pregunta, las posibles respuestas y la respuesta correcta.
    - `check_respuesta(pregunta, respuesta)`: Esta función verifica si la respuesta proporcionada por el usuario es correcta. Toma como entrada la pregunta y la respuesta del usuario, y compara la respuesta del usuario con la respuesta correcta almacenada en el diccionario de preguntas. Devuelve True si la respuesta es correcta y False en caso contrario.

2. **Parte del Cliente (cliente.ipynb)**
    - **Inicialización y Configuración:** Se establecen las constantes `MAX_TIME_WAITING` y `NUM_QUESTIONS` para definir el tiempo máximo de espera y el número de preguntas que el cliente responderá, respectivamente. Se inicializa un socket UDP para la comunicación con el servidor.
   - **Juego:** En un bucle, el cliente envía un mensaje al servidor indicando que está listo para jugar (*Ready to play*). Luego, recibe preguntas del servidor, muestra las preguntas y opciones de respuesta al usuario, envía las respuestas del usuario al servidor y recibe los resultados del servidor. Durante este proceso, la puntuación del usuario se actualiza en función de las respuestas correctas.
   - **Finalización:** Después de responder todas las preguntas, el cliente envía un mensaje de salida al servidor (*Exit*) y muestra la puntuación final al usuario.

3. **Parte del Servidor**
    - **Recepción de Solicitudes del Cliente:** El servidor espera solicitudes de los clientes para enviar preguntas y recibir respuestas.
    - **Envío de Preguntas y Recepción de Respuestas:** El servidor recibe la solicitud del cliente, invoca a la API para obtener una pregunta aleatoria, la envía al cliente y espera la respuesta.
    - **Evaluación de Respuestas:** El servidor compara la respuesta del cliente con la respuesta correcta y envía el resultado de vuelta al cliente.

4. **Funciones Auxiliares (funciones.py)**
    - `send_to_server(message, number_client, ip_address, port_number, socket_cliente)`: Esta función envía un mensaje al servidor utilizando un socket UDP proporcionado. Toma el mensaje, el número de cliente, la dirección IP y el número de puerto del servidor, así como el socket del cliente como entrada.
    
    - `receive_from_server(socket_cliente)`: Esta función recibe un mensaje del servidor utilizando el socket UDP proporcionado. Retorna los bytes recibidos del servidor.
## Ejecución del código 
1. Abre una terminal o línea de comandos en tu sistema.

2. Clona el repositorio con el siguiente comando:

    ```
    git clone https://github.com/202006359/Practica-1-UDP.git
    ```

3. Inicializa el servidor Jupyter Notebook desde Anaconda.
<img width="249" alt="image" src="https://github.com/202006359/Practica-1-UDP/assets/113789409/8347b6ac-c6fb-42b4-8620-f8b7634689c4">

  
5. Una vez inicializado, dirigite a la proyecto Practica-1-UDP y picha en la carpeta "Entregable". Esto abrirá una ventana del navegador web con el panel de control de Jupyter Notebook. Desde aquí, abre el archivo "servidor.ipynb" y "cliente.ipynb".

6. Ejecuta el código del servidor en Jupyter Notebook ejecutando todas las celdas de código en "servidor.ipynb".

7. Ejecuta el código del cliente en Jupyter Notebook ejecutando todas las celdas de código en "cliente.ipynb".

Una vez que hayas ejecutado ambos códigos, podrás jugar al juego de preguntas y respuestas en el cliente y recibir las preguntas y resultados del servidor. 

## Capturas de pantalla
¡Es fundamental tener en cuenta las mayúsculas y minúsculas a la hora de escribir las respuestas!
<img width="514" alt="image" src="https://github.com/202006359/Practica-1-UDP/assets/113789409/622ffe30-631a-410f-bd3b-1895b2a03d53">



