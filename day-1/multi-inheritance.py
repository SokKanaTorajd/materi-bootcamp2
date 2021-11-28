class Mahasiswa():
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def infoMhs(self):
        print(f"nama mahasiswa= {self.nama}, nim = {self.nim}")

class Dosen():
    def __init__(self, nama, nidn):
        self.nama = nama
        self.nidn = nidn

    def infoDsn(self):
        print(f"nama dosen = {self.nama}, nidn = {self.nidn}")

class Pejabat(Mahasiswa, Dosen):
    def __init__(self, nama, nidn, npp, jabatan):
        Dosen.__init__(self, nama, nidn)
        self.npp = npp
        self.jabatan = jabatan

    def infoPejabat(self):
        print(f"nama rektor = {self.nama}, nidn = {self.nidn}, npp={self.nidn}, jabatan={self.jabatan}")

pjbt = Pejabat("Dr. Drs. Djoko Susilo, S.T., M.T., IPU.", 25238, "0001", 'Rektor Unjaya')
# pjbt.infoMhs()
pjbt.infoDsn()
pjbt.infoPejabat()