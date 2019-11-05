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

# Diccionario de ids
ids = { }

# Gramatica

def p_code(p):
    '''block : TkOBlock TkDeclare start TkCBlock
             | TkOBlock body TkCBlock'''
#            | TkOBlock body2 TkCBlock'''
    #if len(p) == 5: print("Block\nDeclare")
    #else: print("Block")
    if len(p) == 5: 
        p[0] = Node("Block\n Declare", None, "%s" % p[3])
    else: p[0] = Node("Block", None, p[2])
    # para len(p) == 4??
 
def p_body(p):
    '''body : sentence body
            | sentcond body
            | unique
            | terminal'''
    if len(p) == 3: p[0] = Node(p[1], None, p[2])
    else: p[0] = Node(p[1], None, None)

#def p_body2(p):
#   '''body2 : sentence
#            | sentcond'''
    # nodo??

def p_start(p):
    ''' start : declaration start
              | declaration body'''
    p[0] = Node(None, p[1], p[2])

def p_empty(p):
    'empty :'
    pass

def p_declaration(p):
    '''declaration : TkId TkTwoPoints tipo TkSemiColon
                   | TkId TkComma listaid TkTwoPoints tipo TkSemiColon'''
    ids[p[1]] = 0
    if len(p) == 5: p[0] = Node("  Ident: %s" % p[1], None, " Sequencing")
    else: p[0] = Node("  Ident: %s" % p[1], p[3], " Sequencing")
    #print("Ident: %s" % p[1])

def p_listid(p):
    '''listaid : TkId TkComma listaid
               | TkId'''
    ids[p[1]] = 0
    if len(p) == 4: p[0] = Node(None, "  Ident: %s" % p[1], p[3])
    else: p[0] = Node(None, "  Ident: %s" % p[1], None)
    #print("Ident: %s" % p[1])

def p_tipo(p):
    '''tipo : TkInt
            | TkArray TkOBracket TkNum TkSoForth TkNum TkCBracket'''

def p_assign_expr(p):
    'assign : TkId TkAsig expression'
    #print("Asig")
    ids[p[1]] = p[3]
    p[0] = Node("Asig", " Ident: %s" % p[1], " %s" % p[3])

def p_assign_str(p):
    'assign : TkId TkAsig strexp'
    #print("String")
    ids[p[1]] = p[3]
    p[0] = Node("AsigStr", "Ident: %s" % p[1], p[3])

def p_assign_arr(p):
    'assign : TkId TkAsig array'
    #print("Array")
    ids[p[1]] = p[3]
    p[0] = Node("AsigArray", "Ident: %s" % p[1], p[3])

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
        p[0] = Node("Exp\n Plus", "  %s" % p[1], "  %s" % p[3])
    elif p[2] == '-' : 
        #p[0] = p[1] - p[3]
        p[0] = Node("Exp\n Minus", "  %s" % p[1], "  %s" % p[3])
    elif p[2] == '*' : 
        #p[0] = p[1] * p[3]
        p[0] = Node("Exp\n Mult", "  %s" % p[1], "  %s" % p[3])
    elif p[2] == '/' : 
        #p[0] = p[1] / p[3]
        p[0] = Node("Exp\n Div", "  %s" % p[1], "  %s" % p[3])
    elif p[2] == '%' : 
        #p[0] = p[1] % p[3]
        p[0] = Node("Exp\n Mod", "  %s" % p[1], "  %s" % p[3])


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
    p[0] = Node("Exp\n %s" % p[1].capitalize(), "  Ident: %s" % p[3], None)

def p_expression_number(p):
    'expression : TkNum'
    #print("Literal: %d" % p[1])
    #p[0] = p[1]
    p[0] = Node("Literal: %d" % p[1], None, None)

def p_expression_id(p):
    'expression : TkId'
    try:
        p[0] = ids[p[1]]
        p[0] = Node("Ident: %s" % p[1], None, None)
    except LookupError:
        print("Undefined id '%s'" % p[1])
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

    #print("Bool")
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

#def p_boolean_group(p):
#    'boolean : TkOpenPar boolean TkClosePar'
    #p[0] = p[2]
#    p[0] = Node(None, p[2], None)

def p_expression_true(p):
    'expression : TkTrue'
    #p[0] = True
    #print("True")
    p[0] = Node("True", None, None)

def p_expression_false(p):
    'expression : TkFalse'
    #p[0] = False
    #print("False")
    p[0] = Node("False", None, None)


def p_expression_not(p):
    'expression : TkNot expression'
    p[0] = Node("Not", p[2], None)

def p_read(p):
    'read : TkRead TkId'
    #print("Read\nIdent: %s" % p[2])
    # Sequencing en TkSemiColon?
    try:
        p[0] = ids[p[2]]
        p[0] = Node("Read", " Ident: %s" % p[2], None)
    except LookupError:
        print("Undefined id '%s'" % p[2])
        exit(1)

def p_cycle_for(p):
    'gfor : TkFor TkId TkIn expression TkTo expression TkArrow block TkRof'
    try:
        p[0] = ids[p[2]]
        p[0] = Node("For\n In\n  Ident: %s\n  Exp\n   %s\n  Exp\n   %s" % (p[2], p[4], p[6]), " %s" % p[8], None)
    except LookupError:
        print("Undefined id '%s'" % p[2])
        exit(1)
 
def p_cycle_do(p):
    'gdo : TkDo expression TkArrow block TkOd'
    p[0] = Node("Do", p[2], p[4])

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
              | gprintln'''
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
    '''strprint : TkString TkConcat strprint
                | TkId TkConcat strprint empty
                | TkString
                | TkId empty'''
    if (len(p) == 4): 
        #print("Concat\n%s" % p[1])
        p[0] = Node("Concat", "  %s" % p[1], "  %s" % p[3])
    elif len(p) == 5:
        try:
            p[0] = ids[p[1]]
            p[0] = Node("Concat", "  %s" % p[1], "  %s" % p[3])
        except LookupError:
            print("Undefined id '%s'" % p[1])
            exit(1)
    elif len(p) == 3:
        try:
            p[0] = ids[p[1]]
            p[0] = Node("%s" % p[1], None, None)
        except LookupError:
            print("Undefined id '%s'" % p[1])
            exit(1)
    else: p[0] = Node("%s" % p[1], None, None)

def p_error(p):
    print("Syntax error at '%s' in line: %s" % (p.value, p.lineno))
    exit(1)

def parsear(content):
    lexer = lex.lex()
    parser = yacc.yacc()

    out = str(parser.parse(content, lexer=lexer))
    while "\n\n" in out: out = out.replace("\n\n", "\n")
    print(out)
