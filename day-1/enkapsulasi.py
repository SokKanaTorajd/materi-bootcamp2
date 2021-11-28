# class Mahasiswa:
#     # public
#     umur = 0
#
#     # private
#     __usia = 0
#
#     def __init__(self, nama, usia):
#         self.nama = None
#         self.__set_usia(usia)
#
#     def get_usia(self):
#         return self.__usia
#
#     def get_nama(self):
#         return self.nama
#
#     def set_nama(self, nama):
#         self.nama = nama
#
#     #setter
#     def __set_usia(self, usia):
#         if usia >= 0:
#             self.__usia = usia
#         else:
#             self.__usia = 0
#
# mhs1 = Mahasiswa('', 21)

## akses public
# mhs1.umur = 21
# print(mhs1.umur)

## akses private
# print(mhs1.get_usia())
# print(mhs1.get_nama())
# mhs1.set_nama('Ridho')
# print(mhs1.get_nama())

# mhs1.__set_usia(22)

class Mahasiswa():
    def __init__(self, nama, nim, asal):
        # private
        self.__nama = nama
        self.__nim = nim
        self.__asal = asal

mhs = Mahasiswa("Nufia", 1234566, "jakarta")
# print(mhs._Mahasiswa__nama)
# print(mhs._Mahasiswa__nim)
# print(mhs._Mahasiswa__asal)
print(mhs.__nama)
