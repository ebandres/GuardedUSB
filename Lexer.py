# NOT FINISHED

import ply

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

class Lexer(object):
	def __init__(self, source):
		self.source = source

	def t_parse(self):
		tokens = []

		content = self.source.split()
		