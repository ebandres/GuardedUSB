class Node(object):
	def __init__(self, p, lc, rc):
		self.p = p
		self.lc = lc
		self.rc = rc

	def __repr__(self):
		return repr(self.lc) + "\n" + repr(self.p) + "\n" + repr(self.rc)
		
		

# test
if __name__ == '__main__':
	t = Node('+',1,2)
	tt = Node('-',t,3)

	print(tt)