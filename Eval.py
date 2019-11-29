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
        'ASIG': eval_asig,
        'ASIGARR': eval_asigarr,
        'NUM': eval_num,
        'PLUS': eval_exp_bin,
        'MINUS': eval_exp_bin,
        'MULT': eval_exp_bin,
        'DIV': eval_exp_bin,
        'MOD': eval_exp_bin,
        'NOT': eval_not,
        'TRUE': eval_bool_single,
        'FALSE': eval_bool_single
    }
    return switcher.get(arg, lambda: "Invalid")

ids_list = []

def eval_ast(ast):
	# ast es un objeto de tipo Nodo (nuestro arbol)

	# Usamos un switch para buscar que funcion usar
	func = switch(ast.p)
	print("NEXT - ", ast.p)

	# Evaluamos la funcion
	try:
		return func(ast)
	except:
		print("EXCEPT ",ast.p)
		exit(1)

def eval_block(node):
	# BLOCK siempre tiene Nodo en lc, dict en rc

	# Comenzamos un nuevo bloque - agregamos el dict a la lista
	ids_list.append(node.rc)
	#print(node.lc)
	return eval_ast(node.lc)

def eval_start(node):
	# START siempre tiene DECLARE en lc, BODY en rc
	# Ignoramos el DECLARE
	return eval_ast(node.rc)

def eval_body(node):
	'''
	BODY tiene dos casos:
	1 - SENTENCE/SENTCOND y BODY
	2 - UNIQUE/TERMINAL
	SENTENCE y UNIQUE son instrucciones normales
	SENTCOND y TERMINAL son if, for y do
	'''
	# Evaluamos lc
	#print(node.rc)
	func = switch(node.lc.p)
	func(node.lc)
	print(ids_list)
	print("---")
	# Revisamos si se tiene BODY
	if node.rc is not None:
		return eval_body(node.rc)
		#print(node.rc)

def eval_sentence(node):
	# Usaremos esta funcion para todos los nodos donde simplemente tengamos que recorrer a node.lc
	return eval_ast(node.lc)

def eval_asig(node):
	# ASIG (expression) siempre tiene ID en lc y un tipo de EXP en rc
	# Buscamos la id en la tabla (ya se comprobo que esta declarada)
	found_id = inIdsList(ids_list, node.lc)
	
	# Evaluamos la expresion
	exp = eval_ast(node.rc)
	# Actualizamos la tabla
	setIdsList(ids_list, node.lc, exp)

def eval_asigarr(node):
	# ASIGARR siempre tiene ID en lc y ARRAY/ARRFUN en rc
	# Buscamos la id
	found_id = inIdsList(ids_list, node.lc)

	# Evaluamos rc
	# Caso ARRAY
	if node.rc.p == 'ARRAY':
		arr = eval_array(node.rc)
		setIdsList(ids_list, node.lc, Symbol('array', arr, found_id.n, found_id.m))
	# Caso ARRFUN
	elif node.rc.p == 'ARRFUN':
		arr = eval_arrfun(node.rc)

def eval_array(node, l = None):
	# ARRAY siempre tiene EXP en lc e INARRAY en rc
	# Calcularemos INARRAY con esta misma funcion recursivamente

	if l is None: l = []

	# Calculamos la expresion en lc
	exp = eval_ast(node.lc)
	l.append(exp)

	# Revisamos si rc es None y evaluamos
	if node.rc is not None:	eval_array(node.rc, l)
	# Retornamos el arreglo
	return l

def eval_arrfun(node, found_id = None):
	'''
	ARRFUN es un poco mas complicado
	Al principio el nodo contendra ID en lc y Node en rc
	Luego se pasa la el Symbol de la ID como parametro para mantenerla en la recursion
	'''
	if found_id is None:
		# Primera vez que se entra a la funcion, buscamos la id
		# Ya la verificacion que fue declarada se hizo en el parser
		found_id = inIdsList(ids_list, node.lc)
		return eval_arrfun(node.rc, found_id)

	# Segunda+ vez que se entra
	# Ahora tenemos EXP en p, EXP en lc y ARRFUN/None en rc
	
	# Evaluamos la exp del indice
	index = eval_ast(node.p)
	new = eval_ast(node.lc)
	print(index)
	print(new)
	try:
		found_id.set_at(index.value, new)
	except IndexError:
		# No se como encontrar la linea sin tener que modificar todo lo que he hecho
		print("Error: array index out of bounds")
		exit(1)

	# Ahora revisamos si se hacen mas ARRFUN
	if node.rc is not None: return eval_arrfun(node.rc, found_id)

def eval_num(node):
	# Un nodo NUM tiene al Symbol en sp, lo retornamos
	return node.sp

def eval_exp_bin(node):
	# EXP BIN siempre tiene EXP en lc y EXP en rc
	# Evaluamos las EXP
	exp1 = eval_ast(node.lc)
	exp2 = eval_ast(node.rc)

	# Retornamos el Symbol resultante
	if node.p == 'PLUS': return exp1 + exp2
	elif node.p == 'MINUS': return exp1 - exp2
	elif node.p == 'MULT': return exp1 * exp2
	elif node.p == 'DIV': return exp1 / exp2
	elif node.p == 'MOD': return exp1 % exp2

def eval_not(node):
	# NOT siempre tiene una EXP BOOL en lc
	# Buscamos la funcion
	func = switch(node.lc.p)
	# Evaluamos
	exp = func(node.lc)
	# Cambiamos
	exp.value = not exp.value
	return exp

def eval_bool_single(node):
	# TRUE/FALSE ya tienen el Symbol en sp
	return node.sp


