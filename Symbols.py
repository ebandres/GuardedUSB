class Symbol(object):
	def __init__(self, var_type, value, n = None, m = None, restricted = False):
		self.var_type = var_type
		self.value = value
		self.restricted = restricted
		if self.var_type == 'array':
			# Si es del tipo array guardamos sus indices
			self.n = n
			self.m = m

	def __repr__(self):
		if self.var_type == 'int':
			return "int: " + str(self.value)
		elif self.var_type == 'array':
			return "array[%d..%d]: %s" % (self.n, self.m, str(self.value))
		elif self.var_type == 'bool':
			return "bool: " + str(self.value)
		return "SYMBOL " + str(self.value)

	def __eq__(self, other):
		return self.value == other.value

	def __ne__(self, other):
		return self.value != other.value

	def __lt__(self, other):
		return self.value < other.value

	def __le__(self, other):
		return self.value <= other.value

	def __gt__(self, other):
		return self.value > other.value

	def __ge__(self, other):
		return self.value >= other.value

	def __neg__(self):
		return Symbol('int', self.value * (-1))

	def __add__(self, other):
		return Symbol('int', self.value + other.value)

	def __sub__(self, other):
		return Symbol('int', self.value - other.value)

	def __mul__(self, other):
		return Symbol('int', self.value * other.value)

	def __div__(self, other):
		return Symbol('int', self.value // other.value)

	def __mod__(self, other):
		return Symbol('int', self.value % other.value)

	def search(self, i):
		# Funcion que busca el indice i (en el rango declarado)
		# Revisamos que el indice este dentro del rango
		if i < self.n or i > self.m:
			raise IndexError
		# Convertimos el indice al rango usado por python 
		i += abs(self.n)
		return self.value[i]

	def set_at(self, i, new):
		if i < self.n or i > self.m:
			raise IndexError
		i += abs(self.n)
		self.value[i] = new
