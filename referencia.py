print('Bug usando listas de objetos.')
# Clase estudiante con un atributo no estático nota
class Estudiante:
	def __init__(self):
		self.nota = 0

# lista de Estudiante
estudiantes = []
e = Estudiante()	# nuevo estudiante
e.nota = 10			
estudiantes.append(e)

# imprimimos la nota del único estudiante en la lista
print('estudiante[0].nota = ', estudiantes[0].nota)

# modificamos la nota
e.nota = 5
# y volvemos a imprimir
print('estudiante[0].nota = ', estudiantes[0].nota)

# Ésto es debido a que e referencia a un objeto Estudiante. La lista guarda la referencia a ese objeto, es decir, la variable e.
# En la línea 17 modificamos el objeto, no la variable e.
# Las siguiente línea no modificarán al objeto porque ahora e referenciará a un nuevo objeto.

e = Estudiante()
e.nota = 100000000
print('estudiante[0].nota = ', estudiantes[0].nota)