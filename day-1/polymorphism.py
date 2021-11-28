# nama = 'Reyhan'
# daftar_mhs = ['reyhan', 'burhan', 'nufia', 'tama']
# prodi = {
#     'nama': 'reyhan',
#     'jurusan': 'sistem informasi',
#     'fakultas': 'ftti'
# }
#
# print(len(nama))
# print(len(daftar_mhs))
# print(len(prodi))


class Mahasiswa():
    def id(self):
        print('1xxxxxx')

    def nama(self):
        print('nama-mhs')

    def prodi(self):
        print('prodi-mhs')

class Dosen():
    def id(self):
        print('381xxxx')

    def nama(self):
        print('nama-dosen')

mhs = Mahasiswa()
dsn = Dosen()

# mhs.id()
# mhs.nama()
# dsn.id()
# dsn.nama()

def info(obj):
    obj.id()
    obj.nama()

info(mhs)
print()
info(dsn)

# coba buatlah class polymorphism dari atlet olahraga yang kalian ketahui.
# methodnya ada skill, bidang
