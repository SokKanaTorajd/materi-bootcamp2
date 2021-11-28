class Esport:
	def skill(self):
		print('user mage')
	def bidang(self):
		print('mid laner')
	def nama(self):
		print('Rrq Lemon :)')

class SepakBola:
	def skill(self):
		print('high dribell')
	def bidang(self):
		print('striker')
	def nama(self):
		print('Ronaldo')

ml = Esport()
sb = SepakBola()


for apalah in (ml, sb):
	apalah.skill()
	apalah.bidang()
	apalah.nama()