class Perhitungan():
	def __init__(self, bil1, bil2):
		self.bil1 = bil1
		self.bil2 = bil2
		print(f"bilangan 1 : {self.bil1}, bilangan 2 : {self.bil2}")
	def perkalian(self):
		hasil = self.bil1 * self.bil2
		print(f"perkalian : {hasil}")
	def pembagian(self):
		hasil = self.bil1 / self.bil2
		print(f"pembagian : {hasil}")
	def penjumlahan(self):
		hasil = self.bil1 + self.bil2
		print(f"penjumlahan : {hasil}")
	def pengurangan(self):
		hasil = self.bil1 - self.bil2
		print(f"pengurangan : {hasil}")

hitung = Perhitungan(12,5)
hitung.perkalian()
hitung.pembagian()
hitung.penjumlahan()
hitung.pengurangan()