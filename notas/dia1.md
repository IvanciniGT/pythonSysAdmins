# Python

Lenguaje de programación
Lenguaje:
    - Sintaxis      <<<< Forma de escribirlo. Funciones que realizan los vocablos dentro de una expresión.
    - Gramatica     <<<< Tipos de vocablos que podemos usar
------------------
    - Semantica     <<<< El significado cada uno de esos vocablos
    
Características de python:
- INTERPRETADO vs Compilados:
    Quien ejecuta las instrucciones es el SO. EL SO entiende su propio lenguaje.
- No precisa definir variables
- Es de tipado dinámico vs lenguajes de tipado estático
    - En un lenguaje de tipado estático, una variable no puede apuntar más que a un determinado tipo de dato, 
       predefinido a la hora de definir la variable 
    - En un lenguaje de tipado dinámico, una variable puede apuntar a cualquier tipo de dato, 
       sin necesidad de definirlo previamente y además variable en el tiempo

Traducción estática: Compilación 
    - Antes de mandar el programa, antes se le hace un analisis exhaustuivo donde se identifican errores
    - Mejor rendimiento
Traducción en tiempo de ejecución: Interpretación
    - Más facilidad a la hora de distribuir el software

Qué interprete o intepretes usamos en python?
>> python/python3: CYTHON: Es un interprete de Python escrito en lenguaje C
        Solo permite usar una única CPU de la máquina <<<
>> jython
>> pypy

## Para qué usamos python. Casos de uso comunes.
- Data analytics <<< numpy pandas skylearn tensorflow theras. Esas librerias están escritas en C
- Automatización
    - Tareas de administración de sistemas
    - Testing
- Monitorización
- Inteligencia artificial

PYTHON Es un lenguaje muy sencillo de aprender. Con una sintaxis muy simple (al compararla con otros lenguajes)

## VARIABLE
- Un espacio de memoria donde almacenamos un valor.... RUINA !!!! GIGANTESCA !!!!
- Referencia a un espacio de memoria donde almacenamos un valor

Ejemplo:
    TEXTO = "17"
    TEXTO = 17
    TEXTO = True
    
    NUMERO > VARIABLE
    =      > OPERADOR     (SEMANTICA := >>>> ASIGNACION)
    17     > VALOR
Qué cosas hace esta linea de código?
    [17]       1º    Reserva un espacio de memoria para guardar el 17 y guarda el 17 en ese espacio de memoria
    [NUMERO]   2º    Crear una variable llamada NUMERO
    [=]        3º    Referenciar desde la variable al espacio de memoria donde está el número 17
    
Ejemplo2:
    NUMERO = 22
Qué cosas hace esta linea de código?
    [22]       1º    Reserva un espacio de memoria para guardar el 22 y guarda el 22 en ese espacio de memoria
        PREGUNTA: El 22 se guarda sobreescribiendo el 17?    El 22 se guarda en otro sitio de la RAM
        ¿Cuantas cosas hay en la RAM? 17 y 22
    [NUMERO]   2º    Reuso la variable NUMERO que ya existe
    [=]        3º    La variable NUMERO CAMBIA (VARIA) a donde referencia... 
                     Ahora referencia a la zona de memoria donde está guardado el 22
    

## TIPOS:
    Vamos a estar guardando cosas en la RAM... Cosas de diferente naturaleza:
        Números
            Enteros
                Rango completo
                Positivos
                En el rango del 0-255
        Textos
        Fechas
        Fecha y Hora
    Los datos de un determinado tipo, el que sea, se guardan en la memoria como bytes (0001110001010101010)
    
Hay determinados lenguajes que me obligan a ir eliminando EXPLICITAMENTE la basura que queda en la RAM: C
Hay lenguajes que automaticamente detectan la BASURA que voy dejando en la RAM y la borran ellos. JAVA, PYTHON
    Garbage Collector
    
Software
    SO
    Driver
    Aplicación
    Script          <<<<< Un programita muy sencillo, que ejeuta una serie de instrucciones y termina.
    Demonio             <<
    Servicio            <<
    
Que aporta PYTHON frente a lenguajes como BASH (SH) o PowerShell de Miscrosoft?
    Dispone de muchas librerias que hacen funciones (calculo, comunicar con otros sistemas...)
    Orientación a objetos <
    Independencia de la plataforma - Portabilidad
    