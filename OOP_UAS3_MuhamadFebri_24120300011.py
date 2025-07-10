# OOP_UAS3_MuhamadFebri_24120300011.py

# class dasar
class Person:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

class Coach(Person):
    def __init__(self, nama, umur, jabatan):
        super().__init__(nama, umur)
        self.jabatan = jabatan

class Player(Person):
    def __init__(self, nama, umur, posisi, nomor):
        if umur > 23:
            print("Umur melebihi U-23:", nama)
        super().__init__(nama, umur)
        self.posisi = posisi
        self.nomor = nomor

class Staff(Person):
    def __init__(self, nama, umur, bagian):
        super().__init__(nama, umur)
        self.bagian = bagian

# factory base
class PersonFactory:
    def create_person(self):
        pass

# subclass factory
class CoachFactory(PersonFactory):
    def create_person(self, nama, umur, jabatan):
        return Coach(nama, umur, jabatan)

class PlayerFactory(PersonFactory):
    def create_person(self, nama, umur, posisi, nomor):
        return Player(nama, umur, posisi, nomor)

class StaffFactory(PersonFactory):
    def create_person(self, nama, umur, bagian):
        return Staff(nama, umur, bagian)

# tim
class Team:
    def __init__(self, nama_tim):
        self.nama_tim = nama_tim
        self.head = None
        self.assist = None
        self.pemain = []
        self.staf = []

    def isi_head(self, pelatih):
        if pelatih.jabatan.lower() == "head coach":
            self.head = pelatih

    def isi_assist(self, pelatih):
        if pelatih.jabatan.lower() == "assistant coach":
            self.assist = pelatih

    def tambah_pemain(self, p):
        if len(self.pemain) < 15:
            self.pemain.append(p)
        else:
            print("maks 15 pemain")

    def tambah_staf(self, s):
        self.staf.append(s)

    def tampil(self):
        print("== TIM:", self.nama_tim, "==")
        print("Head Coach:", self.head.nama if self.head else "-")
        print("Asisten Coach:", self.assist.nama if self.assist else "-")
        print("\nPemain:")
        for p in self.pemain:
            print(f"#{p.nomor} {p.nama} - {p.posisi} ({p.umur}th)")
        print("\nStaf:")
        for s in self.staf:
            print(f"{s.nama} ({s.bagian})")


# contoh
if __name__ == "__main__":
    tim = Team("FC Cakrawala Muda")

    # pake factory
    cf = CoachFactory()
    pf = PlayerFactory()
    sf = StaffFactory()

    # pelatih
    tim.isi_head(cf.create_person("Budi", 44, "Head Coach"))
    tim.isi_assist(cf.create_person("Agus", 39, "Assistant Coach"))

    # pemain
    for i in range(1, 16):
        nama = "Pemain " + str(i)
        umur = 20 + (i % 3)
        p = pf.create_person(nama, umur, "Tengah", i)
        tim.tambah_pemain(p)

    # staf
    tim.tambah_staf(sf.create_person("Siti", 29, "Medis"))
    tim.tambah_staf(sf.create_person("Rudi", 35, "Logistik"))

    tim.tampil()
