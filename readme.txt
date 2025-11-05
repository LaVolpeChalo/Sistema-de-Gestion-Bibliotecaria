####Este Programa Esta Hecho Solo Con Propósitos De Aprendizaje####
--El diagrama de la base de datos y su script se encuentran en /src

Para este proyecto utilicé un stack de solo python (Con FreeSimplyGUI) y PostgreSQL ya que son tecnologías que me sentía seguro de
utilizar al momento de comenzarlo. Quize aplicar conocimientos de POO, SQL y python.

Consiste en un gestor de una biblioteca el cual permita registro de personas que deseen utilizar sus servicios, el registro de
los libros que esta posea y la manipulación de ambos (Prestamos y Devoluciones). Es un proyecto pequeño ya que como se diría
coloquialmente "Fue para soltar la mano". Reconozco que podría tener mejoras como:

-Interfaz adaptada a pantallas grandes y con más contenido visual.
-Registrar más de un solo libro con un mismo ISBN.
-Utilización de Base de datos en tiempo real en vez de solo lectura  y sobreescritura .
-Exportación a csv
-Busqueda por Generos
-Busqueda por Editoriales

Si bien la versión actual no posee esas mejoras, no descarto añadirlas a futuro por entretención/pasatiempo.

De todas formas, en el proceso de crear esta aplicación, fue enriquecedor para mi conocimiento, una manera de ponerme a prueba y
fomentarme el estudio de estas tecnologías.


pyinstaller -w --onefile --icon=src/icon.ico --name 'Gestor de Biblioteca' mainGUI.py