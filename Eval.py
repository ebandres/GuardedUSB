import sys
from tree import Node
from Symbols import Symbol
from Parser import inIdsList, setIdsList

# READ: id (lc) =>
## buscar Symbol de id, hacer input() dependiendo del tipo

# Diccionario de funciones
# Implementacion de un switch con un diccionario
# Si no necesitamos hacer nada en la funcion simplemente la usamos para recorrer el arbol
def switch(arg):
    switcher = {
        'BLOCK'   : eval_block,
        'START'   : eval_start,
        'BODY'    : eval_body,
        'SENTENCE': eval_sentence,
        'SENTCOND': eval_sentence,
        'UNIQUE'  : eval_sentence,
        'TERMINAL': eval_sentence,
        'ASIG'    : eval_asig,
        'ASIGARR' : eval_asigarr,
        'ARREV'   : eval_arrev,
        # EXP
        'NUM'   : eval_num,
        'ID'    : eval_id,
        'UMINUS': eval_uminus,
        'GROUP' : eval_group,
        # EXP BIN
        'PLUS'  : eval_exp_plus,
        'MINUS' : eval_exp_minus,
        'MULT'  : eval_exp_mult,
        'DIV'   : eval_exp_div,
        'MOD'   : eval_exp_mod,
        # BOOL EXP
        'NOT'  : eval_not,
        'TRUE' : eval_bool_single,
        'FALSE': eval_bool_single,
        # FUNCTIONS
        'SIZE': eval_exp_size,
        'MIN' : eval_exp_min,
        'MAX' : eval_exp_max,
        'ATOI': eval_exp_atoi,
        # ARITH COMPARE
        'ALT': eval_bexp_less,
        'ALQ': eval_bexp_leq,
        'AGT': eval_bexp_great,
        'AGQ': eval_bexp_geq,
        'AEQ': eval_bexp_eq,
        'ANE': eval_bexp_neq,
        # BOOL COMPARE
        'BOR' : eval_bexp_or,
        'BAND': eval_bexp_and,
        'BEQ' : eval_bexp_beq,
        'BNE' : eval_bexp_bneq,
        # CONTROL
        'IF' : eval_guard,
        'FOR': eval_cycle_for,
        'DO' : eval_cycle_do,
        # PRINTS
        'PRINT'  : eval_print,
        'PRINTLN': eval_println,
        'CONCAT' : eval_concat,
        'STRING' : eval_string,
        'STREXP' : eval_strexp,
        # READ
        'READ': eval_read
    }
    return switcher.get(arg, lambda: "Invalid")

ids_list = []

def eval_ast(ast):
    # ast es un objeto de tipo Nodo (nuestro arbol)

    # Usamos un switch para buscar que funcion usar
    func = switch(ast.p)

    # Evaluamos la funcion
    return func(ast)

def eval_block(node):
    # BLOCK siempre tiene Nodo en lc, dict en rc

    # Comenzamos un nuevo bloque - agregamos el dict a la lista
    ids_list.append(node.rc)
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
    func = switch(node.lc.p)
    func(node.lc)

    # Revisamos si se tiene BODY
    if node.rc is not None:
        return eval_body(node.rc)

def eval_sentence(node):
    # Usaremos esta funcion para todos los nodos donde simplemente tengamos que recorrer a node.lc
    return eval_ast(node.lc)

def eval_asig(node):
    # ASIG (expression) siempre tiene ID en lc y un tipo de EXP en rc
    # Buscamos la id en la tabla (ya se comprobo que esta declarada)
    found_id = inIdsList(ids_list, node.lc)
    
    # Evaluamos la expresion
    exp = eval_ast(node.rc)
    # Se definio la ID, quitamos el flag de undefined
    exp.undefined = False
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
        found_id.value = arr
        found_id.undefined = False
        setIdsList(ids_list, node.lc, found_id)
    # Caso ARRFUN
    elif node.rc.p == 'ARRFUN':
        try:
            arr = eval_arrfun(node.rc)
        except IndexError:
            raise IndexError(node.lineno)

def eval_array(node, l = None):
    # ARRAY siempre tiene EXP en lc e INARRAY en rc
    # Calcularemos INARRAY con esta misma funcion recursivamente

    if l is None: l = []

    # Calculamos la expresion en lc
    exp = eval_ast(node.lc)
    l.append(exp)

    # Revisamos si rc es None y evaluamos
    if node.rc is not None: eval_array(node.rc, l)
    # Retornamos el arreglo
    return l

def eval_arrfun(node, found_id = None):
    '''
    ARRFUN es un poco mas complicado
    Al principio el nodo contendra ID en lc y Node en rc
    Luego se pasa la el Symbol de la ID como parametro para mantenerla en la recursion
    Se podria hacer con una funcion helper ...
    '''
    if found_id is None:
        # Primera vez que se entra a la funcion, buscamos la id
        # Ya la verificacion que fue declarada se hizo en el parser
        found_id = inIdsList(ids_list, node.lc)
        if found_id.undefined:
            raise Exception("Error in line %s: Variable '%s' has not been defined" % (node.lineno, node.lc))
        return eval_arrfun(node.rc, found_id)

    # Segunda+ vez que se entra
    # Ahora tenemos EXP en p, EXP en lc y ARRFUN/None en rc

    # Evaluamos la exp del indice
    index = eval_ast(node.p)
    new = eval_ast(node.lc)

    found_id.set_at(index.value, new)

    # Ahora revisamos si se hacen mas ARRFUN
    if node.rc is not None: return eval_arrfun(node.rc, found_id)

def eval_arrev(node):
    # ARREV siempre tiene ID en lc y EXP en rc
    # Buscamos la ID
    found_id = inIdsList(ids_list, node.lc)
    if found_id.undefined:
        raise Exception("Error in line %s: Variable '%s' has not been defined" % (node.lineno, node.lc))
    # Evaluamos EXP
    exp = eval_ast(node.rc)
    try:
        return found_id.search(exp.value)
    except IndexError:
        raise IndexError(node.lineno)

#### EXP SINGLE ####

def eval_num(node):
    # Un nodo NUM tiene al Symbol en sp, lo retornamos
    return node.sp

def eval_id(node):
    # Un nodo ID tiene la ID en lc, la buscamos y retornamos
    found_id = inIdsList(ids_list, node.lc)
    if found_id.undefined:
        raise Exception("Error in line %s: Variable '%s' has not been defined" % (node.lineno, node.lc))
    return found_id

def eval_uminus(node):
    # UMINUS siempre tendra solamente EXP en lc
    # Evaluamos EXP
    exp = eval_ast(node.lc)
    return -exp

def eval_group(node):
    # En GROUP solo tenemos que evaluar la EXP en lc
    return eval_ast(node.lc)

#### EXP BIN ####
# PLUS, MINUS, MULT, DIV y MOD siempre tienen EXP en lc y EXP en rc

def eval_exp_plus(node):
    # Retornamos el Symbol resultante
    return eval_ast(node.lc) + eval_ast(node.rc)

def eval_exp_minus(node):
    # Retornamos el Symbol resultante
    return eval_ast(node.lc) - eval_ast(node.rc)

def eval_exp_mult(node):
    # Retornamos el Symbol resultante
    return eval_ast(node.lc) * eval_ast(node.rc)

def eval_exp_div(node):
    # Retornamos el Symbol resultante
    denom = eval_ast(node.rc)
    if denom.value == 0:
        raise ZeroDivisionError(node.lineno)
    return eval_ast(node.lc) / denom

def eval_exp_mod(node):
    # Retornamos el Symbol resultante
    return eval_ast(node.lc) % eval_ast(node.rc)

#### EXP BOOL ####

def eval_not(node):
    # NOT siempre tiene una EXP que evalua a BOOL en lc
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

#### FUNCTIONS ####
# SIZE, MAX, MIN y ATOI siempre tendran ID en lc

def eval_exp_size(node):
    # Buscamos la ID, ya sabemos que es de tipo array
    found_id = inIdsList(ids_list, node.lc)
    return Symbol('int', len(found_id.value))

def eval_exp_max(node):
    found_id = inIdsList(ids_list, node.lc)
    return found_id.m

def eval_exp_min(node):
    found_id = inIdsList(ids_list, node.lc)
    return found_id.n

def eval_exp_atoi(node):
    found_id = inIdsList(ids_list, node.lc)
    return found_id.value[0]

##### COMPARES #####
# Siempre tienen EXP en lc y EXP en rc
# ARITH COMP 

def eval_bexp_less(node):
    return Symbol('bool', eval_ast(node.lc) < eval_ast(node.rc))

def eval_bexp_leq(node):
    return Symbol('bool', eval_ast(node.lc) <= eval_ast(node.rc))
    
def eval_bexp_great(node):
    return Symbol('bool', eval_ast(node.lc) > eval_ast(node.rc))
    
def eval_bexp_geq(node):
    return Symbol('bool', eval_ast(node.lc) >= eval_ast(node.rc))
    
def eval_bexp_eq(node):
    return Symbol('bool', eval_ast(node.lc) == eval_ast(node.rc))
    
def eval_bexp_neq(node):
    return Symbol('bool', eval_ast(node.lc) != eval_ast(node.rc))
    
# BOOL COMP

def eval_bexp_or(node):
    return Symbol('bool', eval_ast(node.lc).value or eval_ast(node.rc).value)

def eval_bexp_and(node):
    return Symbol('bool', eval_ast(node.lc).value and eval_ast(node.rc).value)

def eval_bexp_beq(node):
    return Symbol('bool', eval_ast(node.lc).value == eval_ast(node.rc).value)

def eval_bexp_bneq(node):
    return Symbol('bool', eval_ast(node.lc).value != eval_ast(node.rc).value)

#### CONTROL ####

def eval_cycle_for(node):
    # FOR siempre tiene ID en lc, BLOCK en rc y dos EXP en una lista en sp
    # Tomamos el dict del bloque
    block = node.rc
    ids_list.append(block.rc)

    # Obtenemos los extremos del rango
    first = eval_ast(node.sp[0])
    last = eval_ast(node.sp[1])
    # Asignamos el primer valor a la ID
    setIdsList(ids_list, node.lc, first)
    found_id = inIdsList(ids_list, node.lc)
    found_id.undefined = False
    
    # Comenzamos la iteracion
    while found_id <= last:
        # Evaluamos el bloque
        eval_ast(block.lc)

        # Incrementamos la variable de control
        found_id += Symbol('int', 1)
        setIdsList(ids_list, node.lc, found_id)

    # Terminamos la iteracion, hacemos pop
    ids_list.pop()

def eval_cycle_do(node):
    # DO siempre tiene EXP en lc y UNIQUE/BLOCK y GUARD en una lista en rc
    check = True
    while check:
        # Evaluamos el DO como si fuese una GUARD
        check = eval_guard(node)

def eval_guard(node):
    # GUARD siempre tiene EXP en lc y UNIQUE/BLOCK y GUARD en una lista en rc
    # Si una de las guardias se evaluo TRUE retornamos True, si no retornamos false
    # Evaluamos la EXP
    if eval_ast(node.lc).value:
        # Caso EXP1 == TRUE
        # Evaluamos el UNIQUE/BLOCK
        eval_ast(node.rc[0])
        # Si se evaluo un BLOCK, hacemos pop
        if node.rc[0].p == 'BLOCK': ids_list.pop()
        return True
    # Si no es TRUE, revisamos la siguiente GUARD
    elif node.rc[1] is not None:
        return eval_guard(node.rc[1])
    return False

#### PRINTS ####
# PRINT/PRINTLN siempre tienen STRPRINT en lc
# STRPRINT puede ser CONCAT, STRING o STREXP

def eval_print(node):
    tmp = r'%s' % eval_ast(node.lc)
    tmp = tmp.replace('\\n', '\n').replace('\\\\', '\\').replace('\\"', '\"')
    print(tmp)

def eval_println(node):
    tmp = eval_ast(node.lc)
    tmp = tmp.replace('\\n', '\n').replace('\\\\', '\\').replace('\\\"', '\"')
    print(tmp)

def eval_concat(node):
    # CONCAT siempre tiene STRPRINT en lc y rc
    return eval_ast(node.lc) + eval_ast(node.rc)

def eval_string(node):
    # STRING siempre tiene la string en lc    
    return node.lc

def eval_strexp(node):
    # STREXP siempre tiene EXP en lc
    # Evaluamos y retornamos lc
    return str(eval_ast(node.lc))

#### READ ####

def eval_read(node):
    # READ siempre tiene ID en lc
    # Buscamos la ID
    found_id = inIdsList(ids_list, node.lc)
    # Tomamos el input
    # Hacemos loop infinito hasta que se tenga un input valido como dice el enunciado
    while True:
        val = input()
        try:
            if found_id.var_type == 'int':
                # Convertimos el input a int
                val = int(val)
                found_id.value = val
                setIdsList(ids_list, node.lc, found_id)
                break
            elif found_id.var_type == 'array':
                val = val.split(',')
                if len(val) == len(found_id.value):
                    for i in range(0, len(val)):
                        val[i] = int(val[i])
                    found_id.value = val
                    setIdsList(ids_list, node.lc, found_id)
                break
        except:
            pass
