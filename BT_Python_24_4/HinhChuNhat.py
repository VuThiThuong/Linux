class HinhChuNhat:
	def __init__(self,ten,dai,rong):
		self.ten = ten
		self.dai = dai
		self.rong = rong
	def getTen(self):
		return self.ten
	def getDai(self):
		return self.dai
	def getRong(self):
		return self.rong
	def getCV(self):
		return (self.dai+self.rong)*2
	def getDT(self):
		return self.dai*self.rong
	def toString(self):
		print "%s(%d,%d)" %(self.ten, self.dai,self.rong)
		return 0
