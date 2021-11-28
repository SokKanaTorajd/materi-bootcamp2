class Mahasiswa():
    def __init__(self, nama, nim, asal):
        self._nama = nama
        self._nim = nim
        self._asal = asal

    def getAttrMhs(self):
        print(f"{self._nama}, {self._nim}, {self._asal}")

    def setNama(self, nama):
        self._nama = nama

mhs = Mahasiswa('', 1821000, 'Jakarta')
# print(mhs._Mahasiswa_nama)

mhs.getAttrMhs()
mhs.setNama('Nufia')
mhs.getAttrMhs()

# buatlah sebuah class yang bisa menghitung perkalian, pembagian, penambahan, pengurangan
# sifatnya publik dulu aja, klo sudah dikumpul grup. screenshot.