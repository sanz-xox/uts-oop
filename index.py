# Definisi kelas dasar sebagai kelas
class Person:
    def __init__(self, nama, umur):
        self._nama = nama  # variabel publik
        self._umur = umur  # variabel protected

    # getter untuk nama
    def get_name(self):
        return self._nama

    # setter untuk nama
    def set_nama(self, nama):
        if isinstance(nama, str) and nama.strip():
            self._nama = nama
        else:
            print ("Nama harus berupa string yang tidak kosong")

    # getter untuk umur
    def get_umur(self):
        return self._umur

    # setter untuk umur
    def set_umur(self, umur):
        if isinstance(umur, int) and umur > 0:
            self._umur = umur
        else:
            print("Umur harus berupa integer positif")

    def informasi(self):
        print(f"Nama: {self.get_name()}, Umur: {self.get_umur()}")

# Definisi kelas mahasiswa yang mewarisi kelas Person
class Mahasiswa(Person):
    def __init__(self, nama, umur, mahasiswa_id):
        super().__init__(nama, umur)  # mengambil konstruktor dari kelas Person
        self._mahasiswa_id = mahasiswa_id  # variabel privat

    # getter untuk mahasiswa_id
    def get_mahasiswa_id(self):
        return self._mahasiswa_id

    # setter untuk mahasiswa_id
    def set_mahasiswa_id(self, mahasiswa_id):
        if isinstance(mahasiswa_id, str) and mahasiswa_id.strip():
            self._mahasiswa_id = mahasiswa_id
        else:
            print("Mahasiswa ID harus berupa string yang tidak kosong")

    def info_mahasiswa(self):
        print( f"{super().informasi()}, Mahasiswa ID: {self.get_mahasiswa_id()}")

# Membuat objek dan menguji outputnya
mahasiswa = Mahasiswa("yunus", 20, "123456")
print(mahasiswa.info_mahasiswa())

#mengubah informasi mahasiswa
mahasiswa.set_nama("Budi")
mahasiswa.set_umur(21)
mahasiswa.set_mahasiswa_id("654321")

#menampilkn informasi yg telah d perbarui
print(mahasiswa.info_mahasiswa())
