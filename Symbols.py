class Symbol(object):
	def __init__(self, var_type, value, n = None, m = None, restricted = False, undefined = True):
		self.var_type = var_type
		self.value = value
		self.restricted = restricted
		self.undefined = undefined
		if self.var_type == 'array':
			# Si es del tipo array guardamos sus indices
			self.n = n
			self.m = m

	def __repr__(self):
		if self.var_type == 'int':
			return str(self.value)
		elif self.var_type == 'array':
			tmp = ""
			for i in range(self.n, self.m):
				tmp += "%s:%s, " % (i, self.search(i))
			tmp += "%s:%s" % (self.m, self.search(self.m))
			return tmp
		elif self.var_type == 'bool':
			return "true" if self.value else "false"
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
		self.value *= -1
		return self

	def __add__(self, other):
		self.value += other.value
		return self

	def __sub__(self, other):
		self.value -= other.value
		return self

	def __mul__(self, other):
		self.value *= other.value
		return self

	def __div__(self, other):
		self.value //= other.value
		return self

	def __mod__(self, other):
		self.value %= other.value
		return self

	def search(self, i):
		# Funcion que busca el indice i (en el rango declarado)
		# Revisamos que el indice este dentro del rango
		if i < self.n or i > self.m:
			raise IndexError
		# Convertimos el indice al rango usado por python 
		elif len(self.value) == 1:
			return self.value[0]
			
		i += abs(self.n)
		return self.value[i]

	def set_at(self, i, new):
		if i < self.n or i > self.m:
			raise IndexError
		elif len(self.value) == 1:
			self.value[0] = new
		else:
			i += abs(self.n)
			self.value[i] = new
