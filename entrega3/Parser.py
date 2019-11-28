# parser GuardedUSB
# Emmanuel Bandres 14-10071
# Daniela Caballero 14-10140

import ply.yacc as yacc
import ply.lex as lex
import sys
from tree import Node
from Symbols import Symbol
# Del lexer importamos los tokens
from Lexer import *

precedence = (
    ('left', 'TkAsig'),
    ('left', 'TkAnd', 'TkOr'),
    ('nonassoc', 'TkLess', 'TkLeq', 'TkGeq', 'TkGreater'),
    ('left', 'TkPlus', 'TkMinus'),
    ('left', 'TkMult', 'TkDiv', 'TkMod'),
    ('left', 'TkEqual', 'TkNEqual'),
    ('right', 'TkNot'),
    ('left', 'TkOBracket', 'TkCBracket'),
    ('left', 'TkConcat'),
    ('right', 'TkArrow')
    )

# Lista de tablas de simbolos (1 tabla por bloque)
# Ultima posicion es la mas reciente
# Cuando termina el bloque se elimina su entrada respectiva
# Los elementos de las tablas tienen la forma 'var' : SYMBOL
# SYMBOL contiene tipo y valor de la variable
ids_list = []

# Funciones para la lista de tablas

# Busca una entrada en la lista y lo regresa
def inIdsList(list, var):
    for dic in reversed(list):
        try:
            tmp = dic[var]
            return tmp
        except LookupError:
            pass
    return None

# Busca una entrada y la cambia
def setIdsList(list, var, new):
    for dic in reversed(list):
        try:
            tmp = dic[var]
            dic[var] = new
            return True
        except LookupError:
            pass
    return False

# Gramatica

# Variable para crear una tabla, es false cuando se tiene un for ya que creamos la tabla antes
create_table = True

def p_code(p):
    '''block : TkOBlock TkDeclare table start poptable TkCBlock
             | TkOBlock table body poptable TkCBlock'''
    if len(p) == 7: 
        # Creamos la tabla de simbolos para imprimir
        dic = p[5]
        tmp = "    Symbols Table\n"
        for key in dic:
            symb = dic[key]
            if symb.var_type == 'array':
                tmp += "    variable: %s | type: %s[%d..%d]\n" % (key, symb.var_type, symb.n, symb.m)
            else:
                tmp += "    variable: %s | type: %s\n" % (key, symb.var_type)
        p[0] = Node("Block\n Declare\n%s" % tmp, None, "%s" % p[4])
    else: 
        # Creamos la tabla de simbolos para imprimir
        dic = p[4]
        tmp = "    Symbols Table\n"
        for key in dic:
            symb = dic[key]
            if symb.var_type == 'array':
                tmp += "    variable: %s | type: %s[%d..%d]\n" % (key, symb.var_type, symb.n, symb.m)
            else:
                tmp += "    variable: %s | type: %s\n" % (key, symb.var_type)
        p[0] = Node("Block\n%s" % tmp, None, p[3])

def p_table(p):
    'table :'
    global create_table
    # Creamos una tabla para el bloque actual antes de explorar el resto del arbol
    if create_table: ids_list.append({})
    else: create_table = True

def p_poptable(p):
    'poptable :'
    # Al salir de un bloque sacamos la ultima tabla
    p[0] = ids_list.pop()
 
def p_body(p):
    '''body : sentence body
            | sentcond body
            | unique
            | terminal'''
    if len(p) == 3: p[0] = Node(p[1], None, p[2])
    else: p[0] = Node(p[1], None, None)

def p_start(p):
    '''start : secd body'''
    p[0] = Node(None,p[1],p[2])

def p_empty(p):
    'empty :'
    pass

def p_sec_declare(p):
    '''secd : declaration TkSemiColon secd
            | declaration'''
    if len(p) == 4: p[0] = Node(p[1],p[3],None)
    else: p[0] = Node(p[1],None,None)

def p_declaration(p):
    '''declaration : TkId TkTwoPoints tipo 
                   | TkId TkComma listaid TkTwoPoints tipo 
                   | TkId TkComma listaid TkTwoPoints tipo TkComma listatipo'''
    # Revisamos que la variable no haya sido declarada en la tabla actual
    try:
        p[0] = ids_list[len(ids_list) - 1][p[1]]
        print("Error: Variable %s already declared" % p[1])
        exit(1)
    except LookupError:
        pass

    if len(p) == 4:
        # Caso 1 var, 1 tipo
        # Creamos una entrada en la tabla con un valor por defecto
        # p[3] es del tipo Symbol, contiene los atributos tipo y valor
        ids_list[len(ids_list) - 1][p[1]] = p[3]

        p[0] = Node("  Ident: %s" % p[1], None, " Sequencing")

    elif len(p) == 6:
        # Caso n vars, 1 tipo
        # Agregamos la primera id a la tabla
        ids_list[len(ids_list) - 1][p[1]] = p[5]

        # Creamos el arbol para imprimir
        p[0] = Node("  Ident: %s" % p[1], p[3], " Sequencing")

        # Tomamos las ids y las convertimos en una lista
        # Por como se crea el arbol hay que manipularla como string - revisar manera de mejorar?
        tmp = str(p[3])
        while "Ident:" in tmp: tmp = tmp.replace("Ident:", "")
        tmp = tmp.split()
        # Agregamos cada id a la tabla con el valor por defecto
        for var in tmp:
            ids_list[len(ids_list) - 1][var] = p[5]

    else:
        # Caso n vars, n tipos
        # Agregamos la primera id a la tabla
        ids_list[len(ids_list) - 1][p[1]] = p[5]

        p[0] = Node("  Ident: %s" % p[1], p[3], " Sequencing")

        # Revisamos que en caso de declarar varias variables de diferente tipo, que el numero
        # de variables sea igual al numero de tipos
        type_n = Node(p[5], p[7], None).depth_lc()
        # Si el numero no es igual damos error
        if p[0].depth_lc() != type_n: 
            print("Syntax error: number of variables and types in declaration don't match")
            exit(1)

        # Obtenemos la lista de ids como en el caso anterior
        tmp1 = str(p[3])
        # Obtenemos la lista de tipos
        tmp2 = p[7].list_lc([])
        while "Ident:" in tmp1: tmp1 = tmp1.replace("Ident:", "")
        tmp1 = tmp1.split()
        # Le asignamos cada tipo a la variable respectiva en la tabla
        for var, typ in zip(tmp1, tmp2):
            ids_list[len(ids_list) - 1][var] = typ

def p_listid(p):
    '''listaid : TkId TkComma listaid
               | TkId'''
    # Obtenemos la lista de ids y revisamos si ya fue declarada
    try:
        p[0] = ids_list[len(ids_list) - 1][p[1]]
        print("Error: Variable %s already declared" % p[1])
        exit(1)
    except LookupError:
        pass
    
    # Creamos el arbol
    if len(p) == 4: p[0] = Node("  Ident: %s" % p[1], p[3], None)
    else: p[0] = Node(None, "  Ident: %s" % p[1], None)

def p_tipo_int(p):
    'tipo : TkInt'
    # Creamos un simbolo de tipo int con valor por defecto 0
    p[0] = Symbol('int', 0)

def p_tipo_bool(p):
    'tipo : TkBool'
    # Creamos un simbolo de tipo bool con valor por defecto false
    p[0] = Symbol('bool', False)

def p_tipo_array(p):
    'tipo : TkArray TkOBracket TkNum TkSoForth TkNum TkCBracket'
    # Creamos un simbolo de tipo array con valor por defecto 0
    # Verificamos que el segundo numero de la declaracion del array sea mayor al primero
    if p[3] > p[5]: 
        print("Error in array declaration: %s < %s" % (p[5], p[3]))
        exit(1)
    tmp = []
    for i in range(p[3], p[5] + 1):
        tmp.append(Symbol('int', 0))
    p[0] = Symbol('array', tmp, p[3], p[5])

def p_listtipo(p):
    '''listatipo : tipo TkComma listatipo
                 | tipo'''
    # Creamos el arbol. Como p[1] lleva a tipo, p[1] es un Symbol
    if len(p) == 4: p[0] = Node(p[1], p[3], None)
    else: p[0] = Node(p[1], None, None)

def p_assign_expr(p):
    'assign : TkId TkAsig expression'
    # Revisamos que la variable en p[1] haya sido declarada
    found_id = inIdsList(ids_list, p[1])
    if found_id is None:
        print("Undefined id '%s' in line %s" % (p[1], p.lineno(1)))
        exit(1)
    elif found_id.restricted:
        print("Error: control variable %s is being modified in line %s" % (p[1], p.lineno(2)))
        exit(1)

    # Revisamos que el tipo de p[1] sea igual al tipo de p[3]
    if inIdsList(ids_list, p[1]).var_type == p[3].sp.var_type:
        # Asignamos el valor
        setIdsList(ids_list, p[1], p[3].sp)
    else:
        print("Error: TypeError in line %s" % p.lineno(1))
        exit(1)

    p[0] = Node("Asig", " Ident: %s" % p[1], " %s" % p[3])


def p_assign_arr(p):
    'assign : TkId TkAsig array'
    # Buscamos la id en las tablas
    found_id = inIdsList(ids_list, p[1])
    if found_id is None:
        print("Undefined id '%s' in line %s" % (p[1], p.lineno(1)))
        exit(1)
    # Si existe, revisamos el tipo
    elif found_id.var_type == 'array' and p[3].sp.var_type == 'array':
        # Asignamos un array a otro array
        if len(found_id.value) != len(p[3].sp.value):
            # Si los tamanos de arreglos no son iguales damos error
            print("Error: array length mismatch in line %s" % p.lineno(2))
            exit(1)
        # Actualizamos la tabla
        setIdsList(ids_list, p[1], p[3].sp)

        p[0] = Node("Asig", " Ident: %s" % p[1], p[3])
    else:
        print("Error: TypeError in line %s" % p.lineno(1))
        exit(1)

def p_array(p):
    '''array : expression TkComma inarray
             | TkId arrayfun'''
    if len(p) == 4: 
        if p[1].sp.var_type != 'int':
            print("Error: TypeError in line %d" % p.lineno(2))
            exit(1)
        # Caso lista de numeros
        p[0] = Node(Symbol('int', p[1].sp.value), p[3], None)

        # Creamos un Symbol de tipo array con el arreglo nuevo
        found_id = inIdsList(ids_list, p[-2])
        tmp = Symbol('array', [p[0].p] + p[3].list_lc(), found_id.n, found_id.m)
        # Se lo asignamos al nodo en el arbol
        p[0].set_sp(tmp)
    else: 
        # Caso array fun
        p[0] = Node(None , None, p[2], p[2].sp)

def p_arrayfn(p):
    '''arrayfun : TkOpenPar expression TkTwoPoints expression TkClosePar arrayfunhelper arrayfun
                | TkOpenPar expression TkTwoPoints expression TkClosePar'''
    # Revisamos que las expresiones sean enteros
    if p[2].sp.var_type != 'int' or p[4].sp.var_type != 'int':
        print("Error: TypeError in line %d" % p.lineno(1))
        exit(1)

    # Revisamos que el indice este en el rango
    try:
        inIdsList(ids_list, p[-1]).search(p[2].sp.value)
    except IndexError:
        print("Error: array index out of bounds in line %d" % p.lineno(1))
        exit(1)

    # Como en esta entrega no nos importa el resultado solo creamos el arbol con el Symbol original
    if len(p) == 8: p[0] = Node(" AsigArray\n  Ident: %s\n  %s" % (p[-1], p[2]), "  %s" % p[4], p[7], inIdsList(ids_list, p[-1]))
    else: p[0] = Node(" AsigArray\n  Ident: %s\n  %s" % (p[-1], p[2]), "  %s" % p[4], None, inIdsList(ids_list, p[-1]))

def p_arrayfnh(p):
    'arrayfunhelper :'
    # Guardamos la id para usarla en las arrayfun recursivas
    p[0] = p[-6]

def p_iarray(p):
    '''inarray : expression TkComma inarray
               | expression'''
    # Revisamos el tipo de la expression
    if p[1].sp.var_type != 'int':
        print("Error: TypeError in line %d" % p.lineno(2))
        exit(1)
    # Creamos simbolos con los numeros dados
    if len(p) == 4: p[0] = Node(p[1].sp, p[3], None)
    else: p[0] = Node(p[1].sp, None, None)

def p_expression_bin(p):
    '''expression : expression TkPlus expression
                  | expression TkMinus expression
                  | expression TkMult expression
                  | expression TkDiv expression
                  | expression TkMod expression'''
         
    # Revisamos que el tipo de las expresiones sea entero                                      
    if p[1].sp.var_type != 'int' or p[3].sp.var_type != 'int':
        print("Error: TypeError in line %s" % p.lineno(2))
        exit(1)

    # Creamos el arbol y le asignamos un Symbol nuevo con el resultado de la op
    if p[2] == '+'   :
        p[0] = Node("Exp\n Plus", "  %s" % p[1], "  %s" % p[3], Symbol('int', p[1].sp.value + p[3].sp.value))
    elif p[2] == '-' : 
        p[0] = Node("Exp\n Minus", "  %s" % p[1], "  %s" % p[3], Symbol('int', p[1].sp.value - p[3].sp.value))
    elif p[2] == '*' : 
        p[0] = Node("Exp\n Mult", "  %s" % p[1], "  %s" % p[3], Symbol('int', p[1].sp.value * p[3].sp.value))
    elif p[2] == '/' : 
        if p[3].sp.value == 0:
            print("Error: Divide by zero in line %d" % p.lineno(2))
            exit(1)
        p[0] = Node("Exp\n Div", "  %s" % p[1], "  %s" % p[3], Symbol('int', int(p[1].sp.value / p[3].sp.value)))
    elif p[2] == '%' : 
        p[0] = Node("Exp\n Mod", "  %s" % p[1], "  %s" % p[3], Symbol('int', p[1].sp.value % p[3].sp.value))


def p_expression_group(p):
    'expression : TkOpenPar expression TkClosePar'
    # Creamos el arbol con el valor del Symbol
    p[0] = Node(p[2], None, None, p[2].sp)

def p_expression_fun(p):
    '''expression : TkSize TkOpenPar TkId TkClosePar
                  | TkMax TkOpenPar TkId TkClosePar
                  | TkMin TkOpenPar TkId TkClosePar
                  | TkAtoi TkOpenPar TkId TkClosePar'''
    found_id = inIdsList(ids_list, p[3])
    if found_id is None:
        print("Undefined id '%s' in line %s" % (p[1], p.lineno(1)))
        exit(1)
    elif found_id.var_type == 'array':
        # Si la variable a la que se le aplica la funcion es un arreglo vemos cual fun usamos
        if p[1] == 'size':
            # Devuelve el tamano del arreglo
            p[0] = Node("ArithExp\n %s" % p[1], " Ident: %s" % p[3], None, Symbol('int', len(found_id.value)))
        elif p[1] == 'max':
            # Devuelve el maximo (asumimos que se devuelve es el valor maximo, no el indice en donde esta)
            p[0] = Node("ArithExp\n %s" % p[1], " Ident: %s" % p[3], None, Symbol('int', max(found_id.value).value))
        elif p[1] == 'min':
            # Igual que en max pero para el min
            p[0] = Node("ArithExp\n %s" % p[1], " Ident: %s" % p[3], None, Symbol('int', min(found_id.value).value))
        elif p[1] == 'atoi':
            # REVISAR EN ENUNCIADO - devuelve int si el arreglo es de tamano 1?
            if len(found_id.value) > 1:
                print("Error: atoi recieves an array of length = 1. Array length mismatch in line %d" % p.lineno(1))
                exit(1)
            p[0] = Node("ArithExp\n %s" % p[1], " Ident: %s" % p[3], None, Symbol('int', len(found_id.value)))

def p_expression_number(p):
    '''expression : TkNum
                  | TkId TkOBracket expression TkCBracket'''
    if len(p) == 2: 
        # Caso 1 Creamos el arbol con el Symbol del int
        p[0] = Node(" Literal: %s" % p[1], None, None, Symbol('int', p[1]))
    else: 
        # Caso array[exp]
        found_id = inIdsList(ids_list, p[1])
        if found_id is None:
            print("Undefined id '%s' in line %s" % (p[1], p.lineno(1)))
            exit(1)
        elif found_id.var_type == 'array' and p[3].sp.var_type == 'int':
            # La variable es de tipo array y la expresion es int
            try:
                # Buscamos la expresion en el arreglo
                p[0] = Node("EvalArray", "  Ident: %s " % p[1], " %s" % p[3], Symbol('int', found_id.search(p[3].sp.value)))
            except IndexError:
                print("Error: Index out of bounds in line %s" % p.lineno(1))
                exit(1)

def p_expression_id(p):
    'expression : TkId'
    # Buscamos valor de la id para asignar
    found_id = inIdsList(ids_list, p[1])
    if found_id is None:
        print("Undefined id '%s' in line %s" % (p[1], p.lineno(1)))
        exit(1)

    p[0] = Node("Ident: %s" % p[1], None, None, found_id)


def p_boolean_exp(p):
    '''expression : expression TkLess expression
                  | expression TkLeq expression
                  | expression TkGeq expression
                  | expression TkGreater expression
                  | expression TkOr expression
                  | expression TkAnd expression
                  | expression TkEqual expression
                  | expression TkNEqual expression'''
    # Revisamos que el tipo de las expresiones sea entero                                      
    if p[1].sp.var_type != p[3].sp.var_type:
        print("Error: TypeError in line %s" % p.lineno(2))
        exit(1)

    # Operaciones booleanas para los ints
    if p[1].sp.var_type == 'int':
        if p[2] == '<': 
            p[0] = Node("BoolExp\n  ArithLess", "   %s" % p[1], "   %s" % p[3], Symbol('bool', p[1].sp.value < p[3].sp.value))
        elif p[2] == '<=': 
            p[0] = Node("BoolExp\n  ArithLeq", "   %s" % p[1], "   %s" % p[3], Symbol('bool', p[1].sp.value <= p[3].sp.value))
        elif p[2] == '>=': 
            p[0] = Node("BoolExp\n  ArithGeq", "   %s" % p[1], "   %s" % p[3], Symbol('bool', p[1].sp.value >= p[3].sp.value))
        elif p[2] == '>' : 
            p[0] = Node("BoolExp\n  ArithGreater", "   %s" % p[1], "   %s" % p[3], Symbol('bool', p[1].sp.value > p[3].sp.value))
        elif p[2] == '==': 
            p[0] = Node("BoolExp\n  ArithEqual", "   %s" % p[1], "   %s" % p[3], Symbol('bool', p[1].sp.value == p[3].sp.value))
        elif p[2] == '!=': 
            p[0] = Node("BoolExp\n  ArithNotEqual", "   %s" % p[1], "   %s" % p[3], Symbol('bool', p[1].sp.value != p[3].sp.value))
    else:
        # Operaciones entre bools
        if p[2] == '\\/': 
            p[0] = Node("BoolExp\n  BoolOr", "   %s" % p[1], "   %s" % p[3], Symbol('bool', p[1].sp.value or p[3].sp.value))
        elif p[2] == '/\\': 
            p[0] = Node("BoolExp\n  BoolAnd", "   %s" % p[1], "   %s" % p[3], Symbol('bool', p[1].sp.value and p[3].sp.value))
        elif p[2] == '==': 
            p[0] = Node("BoolExp\n  BoolEqual", "   %s" % p[1], "   %s" % p[3], Symbol('bool', p[1].sp.value == p[3].sp.value))
        elif p[2] == '!=': 
            p[0] = Node("BoolExp\n  BoolNotEqual", "   %s" % p[1], "   %s" % p[3], Symbol('bool', p[1].sp.value != p[3].sp.value))

def p_expression_true(p):
    'expression : TkTrue'
    # Creamos el arbol y un Symbol con True
    p[0] = Node(" Bool: true", None, None, Symbol('bool', True))

def p_expression_false(p):
    'expression : TkFalse'
    # Creamos el arbol y un Symbol con False
    p[0] = Node(" Bool: false", None, None, Symbol('bool', False))

def p_expression_not(p):
    'expression : TkNot expression'
    if p[2].sp.var_type != 'bool':
        print("Error: TypeError in line %d" % p.lineno(1))
        exit(1)
    p[0] = Node("Not", p[2], None, Symbol('bool', not p[2].sp.value))

def p_read(p):
    'read : TkRead TkId'
    # Lo reviso para la proxima entrega
    try:
        p[0] = ids_list[len(ids_list) - 1][p[2]]
        p[0] = Node("Read", " Ident: %s" % p[2], None)
    except LookupError:
        print("Undefined id '%s' in line %s" % (p[2], p.lineno(2)))
        exit(1)

def p_cycle_for(p):
    'gfor : TkFor TkId TkIn expression table2 TkTo expression TkArrow block TkRof'
    # Por ahora no se como se haran las iteraciones, pero permite utilizar una variable
    # que no ha sido declarada
    # Posiblemente necesitaremos modificar las gramaticas para la porxima entrega

    if p[4].sp.value > p[7].sp.value: 
        print("Error: Iteration range error in line %s" % p.lineno(1))
        exit(1)
    p[0] = Node("For\n In\n  Ident: %s\n  Exp\n   %s\n  Exp\n   %s" % (p[2], p[4], p[7]), " %s" % p[9], None)

def p_table_for(p):
    'table2 :'
    # Utilizamos esto para crear la tabla que sera utilizada en el for y no crear una adicional
    global create_table
    create_table = False
    ids_list.append({})
    # Creamos la variable de control en su estado inicial 
    tmp = p[-1].sp
    # La restringimos para que no sea modificada
    tmp.restricted = True
    ids_list[len(ids_list) - 1][p[-3]] = tmp
 
def p_cycle_do(p):
    '''gdo : TkDo expression TkArrow unique guard TkOd
           | TkDo expression TkArrow block guard TkOd'''
    p[0] = Node("Do\n %s" % p[2], p[4], p[5])

def p_if(p):
    '''gif : TkIf expression TkArrow unique guard TkFi  
           | TkIf expression TkArrow block guard TkFi '''
    p[0] = Node("If\n Guard\n  %s" % p[2], p[4], p[5])

def p_sentence(p):
    '''sentence : assign TkSemiColon
                | gprint TkSemiColon
                | gprintln TkSemiColon
                | read TkSemiColon''' 
    p[0] = Node(p[1], None, "Sequencing")

def p_sentence_cond(p):
    '''sentcond : gif TkSemiColon
                | gdo TkSemiColon
                | gfor TkSemiColon'''
    p[0] = Node(p[1],None,"Sequencing")

def p_terminal(p):
    '''terminal : gif
                | gdo
                | gfor'''
    p[0] = Node(p[1],None,None)

def p_unique(p):
    '''unique : assign
              | gprint
              | gprintln
              | read'''
    p[0] = Node(p[1], None, None)

def p_guard(p):
    '''guard : TkGuard expression TkArrow unique guard
             | TkGuard expression TkArrow block guard
             | empty'''
    if len(p) == 6: 
        p[0] = Node(" Guard\n  %s" % p[2], p[4], p[5])

def p_print(p):
    'gprint : TkPrint strprint'
    p[0] = Node(" Print", "  %s" % p[2], None)

def p_println(p):
    'gprintln : TkPrintln strprint'
    p[0] = Node(" Println", "  %s" % p[2], None)

def p_strprint(p):
    '''strprint : strprint TkConcat strprint
                | TkString
                | expression'''
    if len(p) == 4: 
        p[0] = Node("Concat", "  %s" % p[1], "  %s" % p[3])
    else: p[0] = Node(" %s" % p[1], None, None)

def p_error(p):
    print("Syntax error at '%s' in line: %s" % (p.value, p.lineno))
    exit(1)

def parsear(content):
    lexer = lex.lex()
    parser = yacc.yacc()

    out = str(parser.parse(content, lexer=lexer))
    while "\n\n" in out: out = out.replace("\n\n", "\n")
    print(out)

