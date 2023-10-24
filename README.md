Sudoku Modules
==============

Kata sobre programación modular en Python, a partir de uno de los ejercicios propuestos en el _problem set_ de la _Lesson 3: How to Manage Data_ del curso [_Intro to computer science_](https://www.youtube.com/watch?v=9nkR2LLPiYo&list=PLAwxTw4SYaPmjFQ2w9j05WDX8Jtg5RXWW) del Prof. Dave Evans [@evansuva](https://github.com/evansuva) en Udacity. 

Se trata de investigar y comprender los contextos de ejecución al invocar módulos Python.

Por este motivo, la configuración del `sys.path` en el código de `check_Sudoku.py` y los `import`
de las dependencias se han hecho explícitas. Lee los comentarios en el código.

La estructura de directorios y sus nombres tampoco son muy ortodoxas ya que responden a la intención de forzar comportamientos para comprender el sistema de importación de módulos de Python.

No se utiliza una suite de testing, ya que se accede a los casos test utilizando la **reflexión** de Python, accediendo a los mismos como propiedades del objeto módulo `test_Sudoku.py`.

No se utiliza el nombre `test` en el directorio con los casos test porque sino el entorno Python intenta importar desde ese paquete los módulos que no encuentra cuando importamos el contenido del directorio con los casos test (precedencia de nombre).

## Uso

Ejecutar `check_sudoku.py` desde consola en el directorio raíz del proyecto IS OK:

`$ python3 check_sudoku.py`

Ejecutar cada módulo de las funciones SRP desde el contexto `src` IS OK:

`src $ python3 check_Cuadrado.py`

## Menciones

Este programa fue creado con la ayuda de mi profesor David de programación, y además me basé en su programa en `https://github.com/dfleta/sudokuModules/tree/main` y el programa de mi ompañero Samu en `https://github.com/Xpl0itU/sudoku`