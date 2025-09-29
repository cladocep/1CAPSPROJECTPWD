from sqlalchemy import create_engine, insert, update, delete
from sqlalchemy import MetaData, Table, Column, Integer, String, Date, CHAR

metadata = MetaData()
#===== Definisi tabel=====
pasien_claklinik = Table(
    "pasien", metadata,
    Column("id_pasien", String(10), primary_key=True),
    Column("nama_pasien", String(100)),
    Column("tanggal_lahir", Date),
    Column("jenis_kelamin", CHAR(1)),
    Column("layanan", String(50)),
    Column("lama_treatment", Integer),
    Column("biaya", Integer),
    Column("rating", Integer),
    Column("produk_skincare", Integer),
    Column("tanggal_kunjungan", Date)
)
def tambah_pasien(engine):
    data = {
        "id_pasien": input("ID Pasien: "),
        "nama_pasien": input("Nama: "),
        "tanggal_lahir": input("Tanggal lahir (YYYY-MM-DD): "),
        "jenis_kelamin": input("Jenis Kelamin (L/P): "),
        "layanan": input("Layanan: "),
        "lama_treatment": int(input("Lama treatment: ")),
        "biaya": int(input("Biaya: ")),
        "rating": int(input("Rating(1-5): ")),
        "produk_skincare": int(input("Produk skincare: ")),
        "tanggal_kunjungan": input("Tanggal kunjungan (YYYY-MM-DD): ")
    }
    yakin = input("Yakin ingin menambahkan data ini? (y/n): ").strip().lower()
    if yakin == "y":
        with engine.begin() as conn:
                conn.execute(insert(pasien_claklinik).values(**data))
        print("Pasien ditambahkan.")
    else:
        print("Batal menambahkan data.")

def update_pasien(engine):
    pid = input("ID Pasien yang mau di update: ")
    kolom = input("Kolom yang diupdate: ")
    nilai = input("Nilai ingin upadate: ")
    yakin = input(f"Yakin ingin update {kolom} pasien {pid} jadi '{nilai}'? (y/n): ").strip().lower()
    if yakin == "y":
        with engine.begin() as conn:
                conn.execute(update(pasien_claklinik).where(pasien_claklinik.c.id_pasien==pid).values({kolom: nilai}))
        print("Data diupdate.")
    else:
        print("Batal update data.")

def hapus_pasien(engine):
    pid = input("ID Pasien yang mau di hapus: ")
    yakin = input(f"Yakin ingin menghapus pasien {pid}? (y/n): ").strip().lower()
    if yakin == "y":
        with engine.begin() as conn:
            conn.execute(delete(pasien_claklinik).where(pasien_claklinik.c.id_pasien==pid))
        print("Data dihapus.")
    else:
        print("Batal hapus data.")