# Los tipos de datos en Python son dinámicos, es decir, el tipo de una variable se asigna en tiempo de ejecución

# El comando dir() prrmite listar todas las funciones que se pueden ejecutar sobre una variable u objeto

name = "alex"
#print(dir(name))

# Esta salida muestra lo siguiente:
''' ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']'''

# Las listas en Python son el equivalente de vectores dinámicos en lenguajes como C

my_list = []

# print(dir(my_list))
# Esta salida nos muestra todo lo que podemos hacer con una lista; la salida muestra:
"""['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']"""

# Agregando un elemento a la lista
my_list.append("nuevo valor")
# print(my_list)

# La salida es:
""" ['nuevo valor']"""
# Insertando un nuevo elemento
my_list.insert(1,"elemento insertado")
# print(my_list)
# Salida:
""" ['nuevo valor', 'elemento insertado']"""


# Iteradores
# print(iter(my_list))
# Salida:
""" <list_iterator object at 0x7bfcee3010> """

# print(dir(iter(my_list)))
# La salida mostrada es:
""" ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__length_hint__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__']"""

# itera = iter(my_list)
# Esto crea un objeto iterador
# print(next(itera))
# print(next(itera))
# Estas dos salidas muestran los valores de la lista en orden de posicionamiento
# print(next(itera))
# Al solo tener dos elementos en la lista, esto genera una salida StopIteration

# Las tuplas son como las listas, pero no sw puede ni modificar ni agregar más elementos

my_tuple = ('valor 1', 'valor 2')
# print(my_tuple)
# La salida es:
""" ('valor 1', 'valor 2') """

# print(dir(my_tuple))
# Salida: 
""" ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index'] """


# Diccionarios 
my_dictionary = {1: ["lista"], 2: ["tuple"]}
# print(my_dictionary)
# Salida:
"""" {1: ['lista'], 2: ['tuple']} """

# print(dir(my_dictionary))
#Salida:
""" ['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'] """

# Excepciones 
try:
	my_tuple[0] = "12"
except Exception as e:
	#print(str(e))
	pass

# Salida:
""" 'tuple' object does not support item assignment """

# Funciones 
def plus(a,b):
	return a + b
# print(plus(5,4))
# Salida:
""" 9 """
# Importar módulos
# La sentencia import seguida del nombre permite importar un modulo y su contenido.   Esto se puede hacer total o parcial, es decir solo algunas funciones, métodos o clases. Esto lo que hará es mejorar o empeorar el rendimiento de un programa.

