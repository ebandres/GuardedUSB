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
		
		

# test
if __name__ == '__main__':
	t = Node('+',1,2)
	tt = Node(None,None,None)

	print("a")
	print(tt)
	print("b")