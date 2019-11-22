class Symbol(object):
	def __init__(self, var_type, value):
		self.var_type = var_type
		self.value = value

	def __repr__(self):
		if self.var_type == 'int':
			return "  Literal(S): " + str(self.value)
		elif self.var_type == 'array':
			return "  Array(S): " + str(self.value)
		elif self.var_type == 'bool':
			return "  Bool(S): " + str(self.value)
		return "SYMBOL " + str(self.value)
