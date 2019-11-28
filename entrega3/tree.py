class Node(object):
	def __init__(self, p, lc, rc, sp = None, slc = None, src = None):
		self.p = p 		# Parent
		self.lc = lc	# Left Child
		self.rc = rc	# Right Child
		self.sp = sp	# Symbol Parent
		self.slc = slc	# Symbol Left Child
		self.src = src	# Symbol Right Child

	def __repr__(self):
		ret = ""

		if self.p is not None: 
			ret += str(self.p) + "\n"
		if self.lc is not None: 
			ret += str(self.lc) + "\n"
		if self.rc is not None: 
			ret += str(self.rc)

		return ret

	# Innecesario - lo quito despues
	def set_p(self, new):
		self.p = new
		
	def set_lc(self, new):
		self.lc = new

	def set_rc(self, new):
		self.rc = new

	def set_sp(self, new):
		self.sp = new

	def set_slc(self, new):
		self.slc = new

	def set_src(self, new):
		self.src = new

	def depth_lc(self, n = 1):
		# Devuelve la profundidad del arbol en la rama del hijo izq
		try:
			n = self.lc.depth_lc(n + 1)
		except:
			pass
		return n

	def list_lc(self, l = []):
		# Devuelve una lista de los elementos del arbol en la rama del hijo izq
		l.append(self.p)
		try:
			self.lc.list_lc(l)	
		except:
			pass
		return l	

# test
if __name__ == '__main__':
	ttt = Node('+', 3, 4)
	tt = Node('-',ttt,1)
	t = Node('+',tt,2)

	print("a")
	print(t.depth_lc())
	print("b")