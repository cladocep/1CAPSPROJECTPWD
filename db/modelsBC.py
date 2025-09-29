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