# Emmanuel Bandres, 14-10071
# Daniela Caballero, 14-10140

import ply.lex as lex

# Palabras reservadas
reserved = {
        'declare' : 'TkDeclare',
        'print' : 'TkPrint',
        'println' : 'TkPrintln',
        'int' : 'TkInt',
        'in' : 'TkIn',
        'to' : 'TkTo',
        'read' : 'TkRead',
        'if' : 'TkIf',
        'fi' : 'TkFi',
        'do' : 'TkDo',
        'od' : 'TkOd',
        'for' : 'TkFor',
        'rof' : 'TkRof'
        }

# Lista de tokens
tokens = ['TkOBlock','TkCBlock','TkSoForth','TkComma','TkOpenPar','TkClosePar','TkAsig',
          'TkSemiColon','TkArrow','TkGuard','TkPlus','TkMinus','TkMult','TkDiv','TkMod',
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
t_TkString = r'\".*?\"'
t_TkTrue = r'\btrue\b'
t_TkFalse = r'\bfalse\b'

def t_TkId(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reserved.get(t.value,'TkId')    
     return t

def t_TkNum(t):
     r'\d+\b'
     t.value = int(t.value)
     return t 

def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

error_found = False
def t_error(t):
	global error_found
	print("Error: Unexpected character '%s' in row %d, column %d" % (t.value[0], t.lineno, find_column(data, t)))
	error_found = True
	t.lexer.skip(1)

def t_COMMENT(t):
	# Ignoramos los comentarios sin generar un token y aprovechamos
	# para hacer lo mismo con whitespace
    r'//.*| \s'
    pass

def find_column(input, token):
	# Encontramos la columna del token
	line_start = input.rfind('\n', 0, token.lexpos) + 1
	return (token.lexpos - line_start) + 1

# Lexer
lexer = lex.lex()

# Generamos los tokens
def tokenize(content):
	global data
	data = content # Para manejar errores
	lexer.input(content)

	# Tokenize
	generated_tokens = []
	while True:
		tok = lexer.token()
		if not tok: 
			break
		generated_tokens.append(tok)
		
	# Si encontramos un error no imprimimos los tokens, solo los errores
	if not error_found:
		# Si no hay ningun error imprimimos todos los tokens
		for tok in generated_tokens:
			if tok.type == "TkId" or tok.type == "TkNum" or tok.type == "TkString":
				print('%s("%s")' % (tok.type, tok.value), tok.lineno, find_column(content, tok))
			else: 
				print(tok.type, tok.lineno, find_column(content, tok))
		
