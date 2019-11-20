class Node(object):
	def __init__(self, p, lc, rc):
		self.p = p
		self.lc = lc
		self.rc = rc

	def __repr__(self):
		ret = ""

		if self.p != None: 
			ret += str(self.p) + "\n"
		if self.lc != None: 
			ret += str(self.lc) + "\n"
		if self.rc != None: 
			ret += str(self.rc)

		return ret
		
	def depth_lc(self, n = 1):
		try:
			n = self.lc.depth_lc(n + 1)
		except:
			pass
		return n

# test
if __name__ == '__main__':
	ttt = Node('+', 3, 4)
	tt = Node('-',ttt,1)
	t = Node('+',tt,2)

	print("a")
	print(t.depth_lc())
	print("b")