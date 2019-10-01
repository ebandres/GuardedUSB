# NOT FINISHED

import ply

class Lexer(object):
	def __init__(self, source):
		self.source = source

	def t_parse(self):
		tokens = []

		content = self.source.split()
		