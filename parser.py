# parser GuardedUSB
# Emmanuel Bandres 14-10071
# Daniela Caballero 14-10140

import ply.yacc as yacc
import ply.lex as lex
import sys
# Del lexer importamos los tokens
from Lexer import *

precedence = (
    ('left', 'TkAsig'),
    ('nonassoc', 'TkLess', 'TkLeq', 'TkGeq', 'TkGreater'),
    ('left', 'TkPlus', 'TkMinus'),
    ('left', 'TkMult', 'TkDiv', 'TkMod'),
    ('left', 'TkEqual', 'TkNEqual'),
    ('left', 'TkAnd', 'TkOr'),
    ('right', 'TkNot'),
    ('left', 'TkOBracket', 'TkCBracket'),
    ('left', 'TkConcat'),
    ('right', 'TkArrow')
    )

ids = { }

def p_code(p):
    '''block : TkOBlock TkDeclare start TkCBlock
             | TkOBlock body TkCBlock'''
    if len(p) == 5: print("Block\nDeclare")
    else: print("Block")

def p_body(p):
    '''body : assign body
            | gfor body
            | gprint body
            | gprintln body
            | read body
            | empty'''

def p_start(p):
    ''' start : declaration start
              | body'''
              
def p_empty(p):
    'empty :'
    pass

def p_declaration(p):
    '''declaration : TkId TkTwoPoints tipo TkSemiColon
                   | TkId TkComma listaid TkTwoPoints tipo TkSemiColon'''
    ids[p[1]] = 0
    print("Ident: %s" % p[1])

def p_listid(p):
    '''listaid : TkId TkComma listaid
               | TkId'''
    ids[p[1]] = 0
    print("Ident: %s" % p[1])

def p_tipo(p):
    '''tipo : TkInt
            | TkArray TkOBracket TkNum TkSoForth TkNum TkCBracket'''

def p_assign_expr(p):
    'assign : TkId TkAsig expression TkSemiColon'
    print("Asig")
    ids[p[1]] = p[3]

def p_assign_str(p):
    'assign : TkId TkAsig strexp TkSemiColon'
    print("String")
    ids[p[1]] = p[3]

def p_assign_arr(p):
    'assign : TkId TkAsig array TkSemiColon'
    print("Array")
    ids[p[1]] = p[3]

def p_array(p):
    '''array : TkOBracket inarray TkCBracket
             | TkOBracket TkNum TkSoForth TkNum TkCBracket'''

def p_iarray(p):
    '''inarray : TkNum TkComma inarray
               | TkNum'''

def p_expression_str(p):
    '''strexp : TkString TkConcat strexp
              | TkString''' 

def p_expression_bin(p):
    '''expression : expression TkPlus expression
                  | expression TkMinus expression
                  | expression TkMult expression
                  | expression TkDiv expression
                  | expression TkMod expression
                  | expression TkLess expression
                  | expression TkLeq expression
                  | expression TkGeq expression
                  | expression TkGreater expression'''
    print("Exp")
    if p[2] == '+'   :
        print("Plus")
        p[0] = p[1] + p[3]
    elif p[2] == '-' : p[0] = p[1] - p[3]
    elif p[2] == '*' : p[0] = p[1] * p[3]
    elif p[2] == '/' : p[0] = p[1] / p[3]
    elif p[2] == '%' : p[0] = p[1] % p[3]
    elif p[2] == '<' : p[0] = p[1] < p[3]
    elif p[2] == '<=': p[0] = p[1] <= p[3]
    elif p[2] == '>=': p[0] = p[1] >= p[3]
    elif p[2] == '>' : p[0] = p[1] > p[3]

def p_expression_group(p):
    'expression : TkOpenPar expression TkClosePar'
    p[0] = p[2]

def p_expression_fun(p):
    '''expression : TkSize TkOpenPar TkId TkClosePar
                  | TkMax TkOpenPar TkId TkClosePar
                  | TkMin TkOpenPar TkId TkClosePar
                  | TkAtoi TkOpenPar TkId TkClosePar'''
    print(p[1])

def p_expression_number(p):
    'expression : TkNum'
    print("Literal: %d" % p[1])
    p[0] = p[1]

def p_expression_id(p):
    'expression : TkId'
    try:
        p[0] = ids[p[1]]
        print("Ident: %s" % p[1])
    except LookupError:
        print("Undefined id '%s'" % p[1])
        p[0] = 0

def p_read(p):
    'read : TkRead TkId TkSemiColon'
    print("Read\nIdent: %s" % p[2])

def p_cycle_for(p):
    'gfor : TkFor TkId TkIn expression TkTo expression TkArrow block TkRof TkSemiColon'

# Para agregar el do primero debemos tener los booleanos :(
#def p_cycle_do(p):

def p_print(p):
    'gprint : TkPrint strprint TkSemiColon'

def p_println(p):
    'gprintln : TkPrintln strprint TkSemiColon'

def p_strprint(p):
    '''strprint : TkString TkConcat strprint
                | TkId TkConcat strprint
                | TkString
                | TkId'''
    if (len(p) == 4): print("Concat\n%s" % p[1])

def p_error(p):
    print("Syntax error at '%s'" % p.value)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Error: Indicar el nombre del archivo a leer")
        exit(1)
    elif sys.argv[1][len(sys.argv[1]) - 5:] != ".gusb":
        print("Error: El archivo indicado no es un archivo de GuardedUSB")
        exit(1)
    
    # Leemos el contenido del archivo
    content = ""
    with open(sys.argv[1], 'r') as file:
        content = file.read()

    lexer = lex.lex()
    parser = yacc.yacc()
    parser.parse(content, lexer=lexer)