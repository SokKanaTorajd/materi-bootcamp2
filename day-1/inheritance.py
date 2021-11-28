# class MataKuliah():
#     def PBO(self):
#         print('mata kuliah PBO')
#
# class JadwalKuliah(MataKuliah):
#     def DBMS(self):
#         print('mata kuliah DBMS')
#
#
# # jadwal = JadwalKuliah()
# # jadwal.DBMS()
# # jadwal.PBO()
#
# mk = MataKuliah()
# mk.PBO()
# mk.DBMS()

class MataKuliah():
    def __init__(self, matkul, kelas):
        self.matkul = matkul
        self.kelas = kelas

    def cetak(self):
        print('fungsi cetak di class MataKuliah')

    def get_info(self):
        print(f"matkul = {self.matkul}, kelas = {self.kelas}")

class JadwalKuliah(MataKuliah):
    def __init__(self, matkul, kelas, kodeMK):
        MataKuliah.__init__(self, matkul, kelas)
        self.kodeMK = kodeMK

    def cetak2(self):
        print('fungsi cetak2 di class JadwalKuliah')

    def get_info(self):
        print(f"matkul = {self.matkul}, kelas = {self.kelas}, kode mk = {self.kodeMK}")

# mk = JadwalKuliah('PBO', 'Lab3A', 'pbo31')
# mk.cetak()
# mk.cetak2()
# mk.get_info()

matkul = MataKuliah('PBO', 'Lab3A')
matkul.cetak()
matkul.get_info()
matkul.cetak2()

# coba kalian membuat class inheritance bangun datar (superclass).
# ada method menghitung keliling dan luas.
# subclass-nya ada 2 bangun datar yang berbeda.