from abc import ABC, abstractmethod

class Mahasiswa(ABC):
    @abstractmethod
    def tama(self):
        print(1)
    def yusriyah(self):
        print('test!')

class Dosen(Mahasiswa):
    def tama(self):
        print('implementasi')

# mhs = Mahasiswa()
# mhs.yusriyah()
# mhs.tama()

dsn = Dosen()
dsn.tama()
