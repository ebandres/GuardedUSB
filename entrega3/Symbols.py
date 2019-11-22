class Symbol(object):
	def __init__(self, var_type, value, n = None, m = None, restricted = False):
		self.var_type = var_type
		self.value = value
		self.restricted = restricted
		if self.var_type == 'array':
			# Si es del tipo array guardamos sus indices
			# ----------
			# --01234---
			# -10123----
			self.n = n
			self.m = m

	def __repr__(self):
		if self.var_type == 'int':
			return "  Literal: " + str(self.value)
		elif self.var_type == 'array':
			return "  Array[%d..%d]: %s" % (self.n, self.m, str(self.value))
		elif self.var_type == 'bool':
			return "  Bool: " + str(self.value)
		return "SYMBOL " + str(self.value)
