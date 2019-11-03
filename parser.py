# parser GuardedUSB
# Emmanuel Bandres 14-10071
# Daniela Caballero 14-10140

import ply.yacc as yacc
import ply.lex as lex
import sys
from tree import Node
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
    #if len(p) == 5: print("Block\nDeclare")
    #else: print("Block")
    if len(p) == 5: 
        p[0] = Node("Block\n Declare", None, p[3])
        out = str(p[0])
        while "\n\n" in out: out = out.replace("\n\n", "\n")
        print(out)
    else: p[0] = Node("Block", None, p[2])

def p_body(p):
    '''body : sentence body
            | gfor body
            | read body
            | gdo body
            | gif body
            | empty'''
    if len(p) == 3: p[0] = Node(p[1], None, p[2])

def p_start(p):
    ''' start : declaration start
              | body'''
    if len(p) == 3: p[0] = Node(None, p[1], p[2])
    else: p[0] = Node(None, p[1], None)
              
def p_empty(p):
    'empty :'
    pass

def p_declaration(p):
    '''declaration : TkId TkTwoPoints tipo TkSemiColon
                   | TkId TkComma listaid TkTwoPoints tipo TkSemiColon'''
    ids[p[1]] = 0
    if len(p) == 5: p[0] = Node(None, "Ident: %s" % p[1], None)
    else: p[0] = Node(None, "Ident: %s" % p[1], p[3])
    #print("Ident: %s" % p[1])

def p_listid(p):
    '''listaid : TkId TkComma listaid
               | TkId'''
    ids[p[1]] = 0
    if len(p) == 4: p[0] = Node(None, "Ident: %s" % p[1], p[3])
    else: p[0] = Node(None, "Ident: %s" % p[1], None)
    #print("Ident: %s" % p[1])

def p_tipo(p):
    '''tipo : TkInt
            | TkArray TkOBracket TkNum TkSoForth TkNum TkCBracket'''

def p_assign_expr(p):
    'assign : TkId TkAsig expression'
    #print("Asig")
    ids[p[1]] = p[3]
    p[0] = Node("Asig", "Ident: %s\n Exp" % p[1], p[3])

def p_assign_str(p):
    'assign : TkId TkAsig strexp'
    #print("String")
    ids[p[1]] = p[3]
    p[0] = Node("AsigStr", "Ident: %s" % p[1], p[3])

def p_assign_arr(p):
    'assign : TkId TkAsig array'
    #print("Array")
    ids[p[1]] = p[3]
    p[0] = Node("AsigArray", "Ident: %s\n Exp" % p[1], p[3])

def p_array(p):
    '''array : TkOBracket inarray TkCBracket
             | TkOBracket TkNum TkSoForth TkNum TkCBracket'''

def p_iarray(p):
    '''inarray : TkNum TkComma inarray
               | TkNum'''

def p_expression_str(p):
    '''strexp : TkString TkConcat strexp
              | TkString''' 
    if len(p) == 4: p[0] = Node("Concat", p[1], p[3])

def p_expression_bin(p):
    '''expression : expression TkPlus expression
                  | expression TkMinus expression
                  | expression TkMult expression
                  | expression TkDiv expression
                  | expression TkMod expression'''
                                                
    #print("Exp")
    if p[2] == '+'   :
        #print("Plus")
        #p[0] = p[1] + p[3]
        p[0] = Node("Plus", p[1], p[3])
    elif p[2] == '-' : 
        #p[0] = p[1] - p[3]
        p[0] = Node("Minus", p[1], p[3])
    elif p[2] == '*' : 
        #p[0] = p[1] * p[3]
        p[0] = Node("Mult", p[1], p[3])
    elif p[2] == '/' : 
        #p[0] = p[1] / p[3]
        p[0] = Node("Div", p[1], p[3])
    elif p[2] == '%' : 
        #p[0] = p[1] % p[3]
        p[0] = Node("Mod", p[1], p[3])


def p_expression_group(p):
    'expression : TkOpenPar expression TkClosePar'
    #p[0] = p[2]
    p[0] = Node(None, p[2], None)

def p_expression_fun(p):
    '''expression : TkSize TkOpenPar TkId TkClosePar
                  | TkMax TkOpenPar TkId TkClosePar
                  | TkMin TkOpenPar TkId TkClosePar
                  | TkAtoi TkOpenPar TkId TkClosePar'''
    #print(p[1])
    p[0] = Node(p[1].capitalize(), "Ident: %s" % p[3], None)

def p_expression_number(p):
    'expression : TkNum'
    #print("Literal: %d" % p[1])
    #p[0] = p[1]
    p[0] = Node("Literal: %d" % p[1], None, None)

def p_expression_id(p):
    'expression : TkId'
    #try:
    #    p[0] = ids[p[1]]
    #    #print("Ident: %s" % p[1])
    #except LookupError:
    #    print("Undefined id '%s'" % p[1])
    #    p[0] = 0
    p[0] = Node("Ident: %s" % p[1], None, None)

def p_boolean_exp(p):
    '''boolean : expression TkLess expression
               | expression TkLeq expression
               | expression TkGeq expression
               | expression TkGreater expression
               | boolean TkOr boolean
               | boolean TkAnd boolean
               | expression TkEqual expression
               | expression TkEqual boolean
               | boolean TkEqual expression
               | boolean TkEqual boolean
               | expression TkNEqual expression
               | expression TkNEqual boolean
               | boolean TkNEqual expression
               | boolean TkNEqual boolean'''

    #print("Bool")
    if p[2] == '<'    : 
        #p[0] = p[1] < p[3]
        p[0] = Node("Less", p[1], p[3])
    elif p[2] == '<=' : 
        #p[0] = p[1] <= p[3]
        p[0] = Node("Leq", p[1], p[3])
    elif p[2] == '>=' : 
        #p[0] = p[1] >= p[3]
        p[0] = Node("Geq", p[1], p[3])
    elif p[2] == '>'  : 
        #p[0] = p[1] > p[3]
        p[0] = Node("Greater", p[1], p[3])
    elif p[2] == '\\/': 
        #p[0] = p[1] or p[3]
        p[0] = Node("Or", p[1], p[3])
    elif p[2] == '/\\': 
        #p[0] = p[1] and p[3]
        p[0] = Node("And", p[1], p[3])
    elif p[2] == '==' : 
        #p[0] = p[1] == p[3]
        p[0] = Node("Equal", p[1], p[3])
    elif p[2] == '!=' : 
        #p[0] = p[1] != p[3]
        p[0] = Node("NEqual", p[1], p[3])

def p_boolean_group(p):
    'boolean : TkOpenPar boolean TkClosePar'
    #p[0] = p[2]
    p[0] = Node(None, p[2], None)


def p_boolean_true(p):
    'boolean : TkTrue'
    #p[0] = True
    #print("True")
    p[0] = Node("True", None, None)

def p_boolean_false(p):
    'boolean : TkFalse'
    #p[0] = False
    #print("False")
    p[0] = Node("False", None, None)


def p_boolean_not(p):
    'boolean : TkNot boolean'
    p[0] = Node("Not", p[2], None)

def p_read(p):
    'read : TkRead TkId TkSemiColon'
    #print("Read\nIdent: %s" % p[2])
    # Sequencing en TkSemiColon?
    p[0] = Node("Read", "Ident: %s" % p[2], None)

def p_cycle_for(p):
    'gfor : TkFor TkId TkIn expression TkTo expression TkArrow block TkRof TkSemiColon'
    # Si esto no funciona poner p5 y p7 como un nodo, 2do param
    p[0] = Node("For\n In\n  %s\n  %s" % (p[5], p[7]), p[8], None)
 
def p_cycle_do(p):
    'gdo : TkDo boolean TkArrow block TkOd TkSemiColon'
    p[0] = Node("Do", p[2], p[4])

def p_if(p):
    '''gif : TkIf boolean TkArrow unique guard TkFi TkSemiColon
           | TkIf boolean TkArrow block guard TkFi TkSemiColon'''
    p[0] = Node("If\n Guard\n  %s" % p[2], p[4], p[5])

def p_sentence(p):
    '''sentence : assign TkSemiColon
                | gprint TkSemiColon
                | gprintln TkSemiColon''' 
    # Sequencing en TkSemicolon?
    p[0] = Node(p[1], None, None)

def p_unique(p):
    '''unique : assign
              | gprint
              | gprintln'''
    p[0] = Node(p[1], None, None)

def p_guard(p):
    '''guard : TkGuard boolean TkArrow unique guard
             | TkGuard boolean TkArrow block guard
             | empty'''
    if len(p) == 6: 
        p[0] = Node(" Guard\n  %s" % p[2], p[4], p[5])

def p_print(p):
    'gprint : TkPrint strprint'
    p[0] = Node("Print", p[2], None)

def p_println(p):
    'gprintln : TkPrintln strprint'
    p[0] = Node("Println", p[2], None)

def p_strprint(p):
    '''strprint : TkString TkConcat strprint
                | TkId TkConcat strprint
                | TkString
                | TkId'''
    if (len(p) == 4): 
        #print("Concat\n%s" % p[1])
        p[0] = Node("Concat", p[1], p[3])
    else: p[0] = Node(p[1], None, None)

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