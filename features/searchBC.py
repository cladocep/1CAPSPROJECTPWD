from .read_tableBC import get_df

def cari_data(engine):
    kw = input("Keyword (ID/Nama/Layanan): ")
    df = get_df(engine)
    hasil = df[
        df["id_pasien"].astype(str).str.contains(kw, case=False) |
        df["nama_pasien"].str.contains(kw, case=False) |
        df["layanan"].str.contains(kw, case=False)
    ]
    print(hasil if not hasil.empty else "Tidak ditemukan")