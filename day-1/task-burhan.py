class BangunDatar():
	def __init__(self, sisi):
		self.sisi = sisi

	def luas(self):
		pass

	def keliling(self):
		pass

class BangunRuang(self, tinggi):
	def __init__(self, tinggi):
		self.tinggi = tinggi

	def luas_permukaan(self):
		pass

	def volume(self):
		pass

class Kubus(BangunDatar, BangunRuang):
	def __init__(self, sisi, tinggi):
		BangunRuang.__init__(self, tinggi)
		self.sisi = sisi

	def luas(self):
		return self.sisi ** 2

	def luas_permukaan(self):
		return 6*self.luas

	def volume(self):
		return self.sisi**3

class Persegi(BangunDatar):
	def __init__(self, sisi):
		BangunDatar.__init__(self,sisi)
		print(f"sisi = {self.sisi}")

	def luas(self):
		luas = self.sisi * self.sisi
		# luas = self.sisi ** 2
		print(f"luas = {luas}")

	def keliling(self):
		keliling = 4 * self.sisi
		print(f"keliling = {keliling} \n")

class Segitiga(BangunDatar):
	def __init__(self, sisi, tinggi):
		BangunDatar.__init__(self,sisi)
		self.tinggi = tinggi
		self.alas = sisi
		print(f"alas = {self.alas}")
		print(f"tinggi = {self.tinggi}")

	def luas(self):
		luas = 0.5 * self.alas * self.tinggi
		print(f"luas = {luas}")

	def keliling(self):
		keliling = self.sisi + self.sisi + self.sisi
		print(f"keliling = {keliling}")


class SegitigaSamaKaki(BangunDatar, Segitiga):
	def __init__(self, sisi, tinggi):
		Segitiga.__init__(self, sisi, tinggi)

	def luas(self):
		pass

	def keliling(self):
		pass


print('persegi')
persegi = Persegi(4)
persegi.luas()
persegi.keliling()

print('segitiga')
segitiga = Segitiga(10,5)
segitiga.luas()
segitiga.keliling()