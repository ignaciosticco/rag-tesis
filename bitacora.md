Como correr la app:

1) activar el entorno virtual .\.venv\Scripts\Activate
2) luego correr la app: streamlit run .\test_streamlit.py

Para correr un .py o .ipynb hacerlo con el venv activado. 


---------------------------
To do:

1) Investigar como deployar el codigo con streamlit (python version, venv, docker, etc)
2) Investigar como subir las credenciales de forma oculta (https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app)
1) Deployar la app con streamlit




------------------------------
A futuro:
Evaluar al modelo
Tunear los metaparametros
ver que hacer con los graficos (Explorar https://blog.langchain.dev/semi-structured-multi-modal-rag/)
Pasarle tambien los papers que cito en mi tesis. 
Pasarle los papers mios



=======================================================================
Observaciones:

1)
Diferencias con usar chatgpt 3.5 (version online):

Cuando le preguntas: "Mencioname varios modelos de dinamica peatonal"
Te hace una lista de modelos (a pesar de estar fuera del contexto y haberle dicho que conteste que no sabe).

En el experimento que estoy haciendo, cuando le hago esa pregunta me dice que no sabe (lo cual esta bien porque es una pregunta fuera de contexto). 

Conclusion: el chat online es re chamuyero

2) Interesante:

Si al modelo de rag le pregunto: "Que es el flujo?", me responde:

'El flujo se refiere a la cantidad de individuos que atraviesan una cierta sección de un recinto en un determinado intervalo de tiempo.'

A pesar de que el texto que le pase no habla nada del flujo!! solo habla del tiempo de evacuacion. Este es el texto:

Esta tesis estudia la dinámica de multitudes en estado de pánico. Para describir el comportamiento de dichas multitudes se utiliza el modelo de fuerza social de Helbing. En este modelo los individuos se representan como discos blandos que están sometidos a distintos tipos de fuerzas, y la evolución temporal del sistema queda determinada por las ecuaciones de movimiento de la mecánica clásica. La ventaja de este modelo es que permite estudiar fenómenos macroscópicos de la multitud sin perder detalle del carácter microscópico de los individuos que la componen. En primer lugar, se explora el rol de las fuerzas de contacto entre individuos (la fuerza de fricción y la fuerza de repulsión corporal). En particular, se analizan los efectos que produce variar el parámetro de rigidez del cuerpo humano. Se observó que variar dicho parámetro produce efectos muy distintos según el recinto en el cual se encuentre la multitud. En un recinto con puerta angosta (“bottleneck”) el tiempo de evacuación disminuye a medida que la rigidez aumenta. Por otro lado, en un recinto tipo pasillo sucede lo contrario (la velocidad de la multitud disminuye al aumentar la rigidez). Estas diferencias se pueden explicar por el rol que juega la fricción entre individuos, o bien, entre individuos y pared. La primera es decisiva en el caso de “bottlenecks”, mientras que la segunda es más relevante en pasillos.


Conclusion: El modelo de RAG inventa pero muy poquito y muy basado en el contexto. 


3) Interesante: le di todo el resumen de mi tesis y le pregunte: "Segun tu criterio, cual es la etapa mas importante de esta tesis?"

Me contesto:
"La etapa más importante de esta tesis podría ser la calibración de los parámetros utilizando datos empíricos de la vida real para mejorar el modelo..."


Por algun motivo no eligio la etapa 3 y coincide con mi criterio. 


4) Interesante: le pase la portada de la tesis, le pregunte cual es el autor y me dijo Ignacio Sticco (a pesar de que en ningun lado dice explicitamente que soy el autor, lo entendio por contexto). 


5) Las respuestas no son siempre iguales a pesar de que las preguntas y los parametros queden igual. 
A veces tengo que ejecutar 2 veces la misma pregunta para que me conteste bien.

6) No estoy 100% seguro, pero me parece que funciona mejor cuando le paso la tesis en txt que en pdf. 
Hay preguntas que con pdf no me las contesta (me dice que necesita mas info), pero con txt las contesta bien. Hay chances de que sea el factor azaroso que se menciona en el punto de arriba (aunque todo parece indicar que el txt es mejor). 