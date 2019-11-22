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

def p_code(p):
    '''block : TkOBlock TkDeclare table start poptable TkCBlock
             | TkOBlock table body poptable TkCBlock'''
    if len(p) == 7: 
        p[0] = Node("Block\n Declare", None, "%s" % p[4])
    else: p[0] = Node("Block", None, p[3])

def p_table(p):
    'table :'
    # Creamos una tabla para el bloque actual antes de explorar el resto del arbol
    ids_list.append({})

def p_poptable(p):
    'poptable :'
    # Al salir de un bloque sacamos la ultima tabla
    tmp = ids_list.pop()
    print("POPPED LIST")
    print(tmp)
    print("-----------")
 
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
        # p[3] es del tipo Symbol, contiene tipo y valor
        ids_list[len(ids_list) - 1][p[1]] = p[3]

        p[0] = Node("  Ident: %s" % p[1], None, " Sequencing")
        print("LEN 4")
        print(ids_list)
        print("-----")
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
        print("LEN 6")
        print(ids_list)
        print("-----")
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
        print("ELSE")
        print(ids_list)
        print("-----")

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
    #print("Ident: %s" % p[1])

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
    p[0] = Symbol('array', [0] * (p[5] - p[3] + 1))

def p_listtipo(p):
    '''listatipo : tipo TkComma listatipo
                 | tipo'''
    # Creamos el arbol. Como p[1] lleva a tipo, p[1] es un Symbol
    if len(p) == 4: p[0] = Node(p[1], p[3], None)
    else: p[0] = Node(p[1], None, None)

def p_assign_expr(p):
    'assign : TkId TkAsig expression'
    # Revisamos que la variable en p[1] haya sido declarada
    if inIdsList(ids_list, p[1]) == None:
        print("Undefined id '%s' in line %s" % (p[1], p.lineno(1)))
        exit(1)
    print("AAAAA")
    print(p[3])

    try:
        # Revisamos que el tipo de p[1] sea igual al tipo de p[3] - REVISAR QUITAR TRY CUANDO SE TENGAN TODOS LOS TIPOS LISTOS
        if inIdsList(ids_list, p[1]).var_type == p[3].sp.var_type:
            print("!! TRUE !!")
            setIdsList(ids_list, p[1], p[3].sp)
            print("SET", p[1])
            print(ids_list)
            print(type(p[3].sp))
            print("---")
        else:
            print("Error: TypeError2 in line %s" % p.lineno(1))
            exit(1)
    except SystemExit:
        exit(1)
    except:
        print("!! except !!")
    
    p[0] = Node("Asig", " Ident: %s" % p[1], " %s" % p[3])


def p_assign_arr(p):
    '''assign : TkId TkAsig array
              | TkId TkAsig array TkOBracket expression TkCBracket'''
    # Buscamos la id en las tablas
    found_id = inIdsList(ids_list, p[1])
    if found_id == None:
        print("Undefined id '%s' in line %s" % (p[1], p.lineno(1)))
        exit(1)
    # Si existe, revisamos el tipo
    elif found_id.var_type == 'array' and p[3].sp.var_type == 'array':
        if len(found_id.value) != len(p[3].sp.value):
            # Si los tamanos de arreglos no son iguales damos error
            print("Error: array length mismatch in line %s" % p.lineno(2))
            exit(1)
        print("!! TRUE array asig !!")
        setIdsList(ids_list, p[1], p[3].sp)
        print("SET", p[1])
        print(ids_list)
        print(p[3].sp)
        print("---")
    else:
        print("Error: TypeError3 in line %s" % p.lineno(1))
        exit(1)

def p_array(p):
    '''array : TkNum TkComma inarray
             | TkId arrayfun'''
    if len(p) == 4: 
        # Caso lista de numeros
        p[0] = Node(Symbol('int', p[1]), p[3], None)
        # Creamos un Symbol de tipo array con el arreglo nuevo
        tmp = Symbol('array', [p[0].p] + p[3].list_lc())
        # Se lo asignamos al nodo en el arbol
        p[0].set_sp(tmp)
    else: 
        # Caso array fun - POR TERMINAR
        p[0] = Node(" AsigArray" , "  Ident: %s" % p[1], p[2])

def p_arrayfn(p):
    '''arrayfun : TkOpenPar expression TkTwoPoints expression TkClosePar arrayfun
                | TkOpenPar expression TkTwoPoints expression TkClosePar'''
    if len(p) == 7: p[0] = Node("  %s" % p[2], "  %s" % p[4], p[6])
    else: p[0] = Node("  %s" % p[2], "  %s" % p[4], None)

def p_iarray(p):
    '''inarray : TkNum TkComma inarray
               | TkNum'''
    # Creamos simbolos con los numeros dados - CAMBIAR PARA QUE FUNCIONE CON EXPRESIONES Y NO SOLO NUM
    if len(p) == 4: p[0] = Node(Symbol('int', p[1]), p[3], None)
    else: p[0] = Node(Symbol('int', p[1]), None, None)

def p_expression_bin(p):
    '''expression : expression TkPlus expression
                  | expression TkMinus expression
                  | expression TkMult expression
                  | expression TkDiv expression
                  | expression TkMod expression'''
         
    # Revisamos que el tipo de las expresiones sea entero                                      
    if p[1].sp.var_type != 'int' or p[3].sp.var_type != 'int':
        print("Error: TypeError1 in line %s" % p.lineno(2))
        exit(1)

    # Creamos el arbol y le asignamos los Symbol de las expresiones correspondientes (lc y rc)
    # y un Symbol nuevo con el resultado de la op
    if p[2] == '+'   :
        p[0] = Node("Exp\n Plus", "  %s" % p[1], "  %s" % p[3], Symbol('int', p[1].sp.value + p[3].sp.value), p[1].sp, p[3].sp)
    elif p[2] == '-' : 
        p[0] = Node("Exp\n Minus", "  %s" % p[1], "  %s" % p[3], Symbol('int', p[1].sp.value - p[3].sp.value), p[1].sp, p[3].sp)
    elif p[2] == '*' : 
        p[0] = Node("Exp\n Mult", "  %s" % p[1], "  %s" % p[3], Symbol('int', p[1].sp.value * p[3].sp.value), p[1].sp, p[3].sp)
    elif p[2] == '/' : 
        p[0] = Node("Exp\n Div", "  %s" % p[1], "  %s" % p[3], Symbol('int', p[1].sp.value / p[3].sp.value), p[1].sp, p[3].sp)
    elif p[2] == '%' : 
        p[0] = Node("Exp\n Mod", "  %s" % p[1], "  %s" % p[3], Symbol('int', p[1].sp.value % p[3].sp.value), p[1].sp, p[3].sp)


def p_expression_group(p):
    'expression : TkOpenPar expression TkClosePar'
    # Creamos el arbol con el valor del Symbol
    p[0] = Node(p[2], None, None, p[2].sp)

def p_expression_fun(p):
    '''expression : TkSize TkOpenPar TkId TkClosePar
                  | TkMax TkOpenPar TkId TkClosePar
                  | TkMin TkOpenPar TkId TkClosePar
                  | TkAtoi TkOpenPar TkId TkClosePar'''
    # POR COMPLETAR
    try:
        p[0] = ids_list[len(ids_list) - 1][p[3]]
        p[0] = Node("Exp\n %s" % p[1].capitalize(), "  Ident: %s" % p[3], None)
    except LookupError:
        print("Undefined id '%s' in line %s" % (p[3], p.lineno(3)))
        exit(1)

def p_expression_number(p):
    '''expression : TkNum
                  | TkId TkOBracket expression TkCBracket'''
    if len(p) == 2: 
        # Caso 1 Creamos el arbol con el Symbol del int
        p[0] = Node(" Literal: %s" % p[1], None, None, Symbol('int', p[1]))
    else: 
        # Caso array[exp] - POR TERMINAR
        p[0] = Node("EvalArray", "  Ident: %s " % p[1], "  %s" % p[3])

def p_expression_id(p):
    'expression : TkId'
    # POR TERMINAR Buscar valor de la id para asignar
    try:
        p[0] = ids_list[len(ids_list) - 1][p[1]]
        p[0] = Node("Ident: %s" % p[1], None, None)
    except LookupError:
        print("Undefined id '%s' in line %s" % (p[1], p.lineno(1)))
        exit(1)

def p_boolean_exp(p):
    '''expression : expression TkLess expression
                  | expression TkLeq expression
                  | expression TkGeq expression
                  | expression TkGreater expression
                  | expression TkOr expression
                  | expression TkAnd expression
                  | expression TkEqual expression
                  | expression TkNEqual expression'''

    # POR TERMINAR Igual que exp bin pero con booleanos
    if p[2] == '<'    : 
        #p[0] = p[1] < p[3]
        p[0] = Node("Less", "  %s" % p[1], "  %s" % p[3])
    elif p[2] == '<=' : 
        #p[0] = p[1] <= p[3]
        p[0] = Node("Leq", "  %s" % p[1], "  %s" % p[3])
    elif p[2] == '>=' : 
        #p[0] = p[1] >= p[3]
        p[0] = Node("Geq", "  %s" % p[1], "  %s" % p[3])
    elif p[2] == '>'  : 
        #p[0] = p[1] > p[3]
        p[0] = Node("Greater", "  %s" % p[1], "  %s" % p[3])
    elif p[2] == '\\/': 
        #p[0] = p[1] or p[3]
        p[0] = Node("Or", "  %s" % p[1], "  %s" % p[3])
    elif p[2] == '/\\': 
        #p[0] = p[1] and p[3]
        p[0] = Node("And", "  %s" % p[1], "  %s" % p[3])
    elif p[2] == '==' : 
        #p[0] = p[1] == p[3]
        p[0] = Node("Equal", "  %s" % p[1], "  %s" % p[3])
    elif p[2] == '!=' : 
        #p[0] = p[1] != p[3]
        p[0] = Node("NEqual", "  %s" % p[1], "  %s" % p[3])

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
    # POR TERMINAR
    p[0] = Node("Not", p[2], None)

# DE AQUI PA BAJO NI IDEA

def p_read(p):
    'read : TkRead TkId'
    # NI IDEA
    try:
        p[0] = ids_list[len(ids_list) - 1][p[2]]
        p[0] = Node("Read", " Ident: %s" % p[2], None)
    except LookupError:
        print("Undefined id '%s' in line %s" % (p[2], p.lineno(2)))
        exit(1)

def p_cycle_for(p):
    'gfor : TkFor TkId TkIn expression TkTo expression TkArrow block TkRof'
    try:
        p[0] = ids_list[len(ids_list) - 1][p[2]]
        p[0] = Node("For\n In\n  Ident: %s\n  Exp\n   %s\n  Exp\n   %s" % (p[2], p[4], p[6]), " %s" % p[8], None)
    except LookupError:
        print("Undefined id '%s' in line %s" % (p[2], p.lineno(2)))
        exit(1)
 
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
    # Sequencing en TkSemicolon?
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
        #print("Concat\n%s" % p[1])
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

