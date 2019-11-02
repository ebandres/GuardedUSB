# parser GuardedUSB
# Emmanuel Bandres 14-10071
# Daniela Caballero 14-10140

import ply.yacc as yacc
# Del lexer importamos los tokens
from Lexer import tokens

def p_code(p):

	block : TkOBlock TkDeclare declaration TkCBlock
		  | TkOBlock TkDeclare declaration body TkCBlock

def p_declaration(p):

	declaration : TkId TkTwoPoints tipo
				| TkId TkComma declaration

def p_tipo(p):

	tipo : TkInt
		#| el de arreglo

def p_asign(p):

	asign : TkId TkAsig aritexp
		  | TkId TkAsig TkString
		  | TkId TkAsig array

def p_array(p):

	array : TkOBracket inarray TkCBracket
		  | TkOBracket TkNum TkSoForth TkNum TkCBracket

def p_iarray(p):

	inarray : TkNum TkComma inarray
			| TkNum

def p_aritexp(p):

	aritexp : aritexp TkPlus aritexp
	        | aritexp TkMinus aritexp
	        | aritexp TkMult aritexp
	        | aritexp TkDiv aritexp
	        | aritexp TkMod aritexp
	        | aritexp TkLess aritexp
	        | aritexp TkLeq aritexp
	        | aritexp TkGeq aritexp
	        | aritexp TkGreater aritexp
	        | TkOpenPar aritexp TkClosePar
	        | TkNum
	        | TkId
