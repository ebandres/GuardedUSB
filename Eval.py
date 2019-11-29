from tree import Node
from Symbols import Symbol
from Parser import inIdsList, setIdsList

# EVAL
# ARBOL/BLOQUE?, DIC -> DIC
# Crear una funcion que reciba un arbol PONER DIC EN BLOQUE? y evalue los nodos
# Tener lista de dics para encontrar vars y respetar alcance
## Bloque nuevo => append dic del bloque en lista
## Terminar do el bloque => hacer pop en la lista. Reemplazar en nodo del bloque?

# ASIGARR: id (lc), nodo (rc) => ARRAY o ARRFUN
## Asignar resultado de nodo en id

# ARRAY: exp (lc), nodo (rc) =>
## eval exp
## Mientras nodo no sea None, eval nodo.p, reemp nodo por nodo.lc (INARRAY)

# ARRFUN: id (lc), nodo (rc) => 
## en nodo eval expr1 (p) y expr2 (lc) y asignar a id en dic
## (usar funcion que cambie a rango del arreglo)
### si es recursivo (revisar rc) mandar id y nodo2 (nodo.rc), repetir
### (sabemos que es recursivo si nodo.rc no es None)

# ARREV: id (lc), nodo (rc) =>
## eval expr (nodo) luego usar found_id.search(expr.sp.value) y asignar

# GROUP: exp (lc) =>
## eval exp

# NUM: num (lc) =>
## crear Symbol con num

# ID: id (lc) =>
## buscar Symbol de id en lista

# TRUE/FALSE: Symbol (sp) =>
## return sp

# NOT: exp (lc) =>
## eval exp, cambiar y ret

# FOR: id (lc), BLOQUE (rc), expr range (sp) =>
## obtener dic del bloque, calcular expr en sp y crear range (revisar que 1<2)

# DO: expbool (lc), unique/block (rc), guard prox (sp) =>
## si expbool es true => eval unique/block hasta que expbool sea false (eval antes de cada iter)
## si es false => ir a guardia (si no es None)
### GUARD: expbool (lc), unique/block (rc), guard prox (sp) => same

# IF: expbool (lc), unique/block (rc), guard prox (sp) => same pero 1 vez

# PRINT/PRINTLN: strnode (lc) => 
## juntar concat, manip strings (comment en parser)
## anadir \n si es println? revisar como imprimir en misma linea para print normal?

# READ: id (lc) =>
## buscar Symbol de id, hacer input() dependiendo del tipo

# Implementacion de un switch con un diccionario
# Si no necesitamos hacer nada en la funcion simplemente la usamos para recorrer el arbol
def switch(arg):
    switcher = {
        'BLOCK': eval_block,
        'START': eval_start,
        'BODY': eval_body,
        'SENTENCE': eval_sentence,
        'ASIG': eval_asig
    }
    return switcher.get(arg, lambda: "Invalid")

ids_list = []

def eval_ast(ast):
	# ast es un objeto de tipo Nodo (nuestro arbol)

	# Usamos un switch para buscar que funcion usar
	func = switch(ast.p)
	# Evaluamos la funcion
	func(ast)

def eval_block(node):
	# BLOCK siempre tiene Nodo en lc, dict en rc

	# Comenzamos un nuevo bloque - agregamos el dict a la lista
	ids_list.append(node.rc)
	#print(node.lc)
	eval_ast(node.lc)

def eval_start(node):
	# START siempre tiene DECLARE en lc, BODY en rc
	# Ignoramos el DECLARE
	eval_ast(node.rc)

def eval_body(node):
	'''
	BODY tiene dos casos:
	1 - SENTENCE/SENTCOND y BODY
	2 - UNIQUE/TERMINAL
	SENTENCE y UNIQUE son instrucciones normales
	SENTCOND y TERMINAL son if, for y do
	'''
	# Evaluamos lc
	eval_ast(node.lc)
	#eval_ast(node.lc)

def eval_sentence(node):
	# Usaremos esta funcion para todos los nodos donde simplemente tengamos que recorrer a node.lc
	eval_ast(node.lc)

def eval_asig(node):
	# ASIG (expression) siempre tiene ID en lc y un tipo de EXP en rc
	print(node)
	print(inIdsList(ids_list, node.lc))

