class Symbol(object):
	def __init__(self, var_type, value):
		self.var_type = var_type
		self.value = value

	def __repr__(self):
		return "SYMBOL " + str(self.value)
