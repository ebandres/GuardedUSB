# parser GuardedUSB
# Emmanuel Bandres 14-10071
# Daniela Caballero 14-10140

import ply.yacc as yacc
# Del lexer importamos los tokens
from Lexer import tokens

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

#def p_code(p):
#    '''block : TkOBlock TkDeclare declaration TkCBlock
#             | TkOBlock TkDeclare declaration body TkCBlock'''

#def p_declaration(p):
#    '''declaration : TkId TkTwoPoints tipo
#                   | TkId TkComma declaration'''
#
#def p_tipo(p):
#    '''tipo : TkInt
#            | TkArray lo demas'''

def p_assign_expr(p):
    'assign : TkId TkAsig expression'
    names[p[1]] = p[3]
    #print("Asig")

def p_assign_str(p):
    'assign : TkId TkAsig strexp'
    names[p[1]] = p[3]

def p_assign_arr(p):
    'assign : TkId TkAsig array'
    names[p[1]] = p[3]

def p_array(p):
    '''array : TkOBracket inarray TkCBracket
             | TkOBracket TkNum TkSoForth TkNum TkCBracket'''

def p_iarray(p):
    '''inarray : TkNum TkComma inarray
               | TkNum'''

#def p_expression_str(p):


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
    if p[2] == '+'   : p[0] = p[1] + p[3]
    elif p[2] == '-' : p[0] = p[1] - p[3]
    elif p[2] == '*' : p[0] = p[1] * p[3]
    elif p[2] == '/' : p[0] = p[1] / p[3]
    elif p[2] == '%' : p[0] = p[1] / p[3]
    elif p[2] == '<' : p[0] = p[1] / p[3]
    elif p[2] == '<=': p[0] = p[1] / p[3]
    elif p[2] == '>=': p[0] = p[1] / p[3]
    elif p[2] == '>' : p[0] = p[1] / p[3]

def p_expression_group(p):
    'expression : TkOpenPar expression TkClosePar'
    p[0] = p[2]

def p_expression_number(p):
    'expression : TkNum'
    p[0] - p[1]

def p_expression_id(p):
    'expression : TkId'
    try:
        p[0] = ids[p[1]]
    except LookupError:
        print("Undefined id '%s'" % p[1])
        p[0] = 0

def p_error(p):
    print("Syntax error at '%s" % p.value)