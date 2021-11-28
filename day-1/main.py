# class Mahasiswa():
#
#     def __init__(self, nama):
#         self.nama = nama
#
#     def belajar(self, kondisi):
#         print(f"{self.nama} sedang belajar {kondisi}")
#         # print("%s sedang belajar %s"%(self.nama, kondisi))
#         # print(self.nama + " sedang belajar " + kondisi)
#
#     def tidur(self, tempat):
#         print(f"{self.nama} sedang tidur di {tempat}")
#
# mhs1 = Mahasiswa('ridho')
# mhs1.belajar('python')
#
# # ridho = Mahasiswa()
# # ridho.nama = 'ridho'
# # ridho.belajar('python')
#
# # tama = Mahasiswa()
# # tama.nama = 'tama'
# # tama.tidur('kelas')


class Mahasiswa():

    def __init__(this, nama, nim, prodi, asal):
        this.nama = nama
        this.nim = nim
        this.prodi = prodi
        this.asal = asal

    def perkenalan(this):
        print(f"Nama saya {this.nama}, nim {this.nim}, prodi saya {this.prodi}, asal dari {this.asal}")



mahasiswa1 = Mahasiswa("Mohammad Burhanuddin", 123456, "Sistem Informasi", "Kalimantan Barat")
# mahasiswa1.nama = 'Mohammad Burhanuddin'
# mahasiswa1.nim = 123456
# mahasiswa1.prodi = 'Sistem Informasi'
# mahasiswa1.asal = 'Kalimantan Barat'
# print(mahasiswa1.nama, mahasiswa1.nim, mahasiswa1.prodi)
mahasiswa1.perkenalan()