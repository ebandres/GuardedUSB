# NOT FINISHED

import ply.lex as lex

reserved = {
        'declare' : 'TkDeclare',
        'if' : 'TkIf',
        'do' : 'TkDo',
        'od' : 'TkOd',
        'while' : 'TkWhile',
        'for' : 'TkFor',
        'else' : 'TkElse'
        }

tokens = ['TkOBlock','TkCBlock','TkSoForth','TkComma','TkOpenPar','TkClosePar','TkAsig',
          'TkSemicolon','TkArrow','TkGuard','TkPlus','TkMinus','TkMult','TkDiv','TkMod',
          'TkOr','TkAnd','TkNot','TkLess','TkLeq','TkGeq','TkGreater','TkEqual','TkNEqual',
          'TkOBracket','TkCBracket','TkTwoPoints','TkConcat','TkAtoi','TkSize','TkMax',
          'TkMin','TkId','TkNum','TkString','TkTrue','TkFalse'] + list(reserved.values())

# Tokens

t_TkOBlock = r'\|\['
t_TkCBlock = r'\]\|'
t_TkSoForth = r'\.\.'
t_TkComma = r','
t_TkOpenPar = r'\('
t_TkClosePar = r'\)'
t_TkAsig = r':='
t_TkSemiColon = r';'
t_TkArrow = r'-->'
t_TkGuard = r'\[\]'
t_TkPlus = r'\+'
t_TkMinus = r'-'
t_TkMult = r'\*'
t_TkDiv = r'/'
t_TkMod = r'%'
t_TkOr = r'\\/'
t_TkAnd = r'/\\'
t_TkNot = r'!'
t_TkLess = r'<'
t_TkLeq = r'<='
t_TkGeq = r'>='
t_TkGreater = r'>'
t_TkEqual = r'=='
t_TkNEqual = r'!='
t_TkOBracket = r'\['
t_TkCBracket = r'\]'
t_TkTwoPoints = r':'
t_TkConcat = r'\|\|'
t_TkString = r'([\"\'])(?:(?=(\\?))\2.)*?\1'
t_TkTrue = r'\btrue\b'
t_TkFalse = r'\bfalse\b'

def t_TkId(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reserved.get(t.value,'TkId')    
     return t

def t_TkNum(t):
     r'\d+'
     t.value = int(t.value)
     return t 

# Faltan los tokens a ignorar

class Lexer(object):
	def __init__(self, source):
		self.source = source

	def t_parse(self):
		tokens = []

		content = self.source.split()
		
