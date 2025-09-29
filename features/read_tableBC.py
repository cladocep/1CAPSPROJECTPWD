import pandas as pd

NUMERIC_COLS = ["umur", "lama_treatment","biaya", "rating", "produk_skincare"]
CATEG_COLS = ["jenis_kelamin", "layanan"]

# ====Fungsi Read Table====
def get_df(engine):
    try:
        with engine.connect() as conn:
            df = pd.read_sql("SELECT * FROM pasien_claklinik", conn)
            print(df)
        return df
    except Exception as e:
        print("Error di read table:", e)
        return pd.Dataframe()
    
 # export data csv   
def read_table(engine):
    try:
        df = df = pd.read_sql("SELECT * FROM pasien_claklinik", engine)
        print("\n=== Data Pasien ===")
        print(df)

        export = input("\nMau export data ke file? (y/n): ").lower()
        if export == "y":
            df.to_csv("data_pasien.csv", index=False)
            print("Data berhasil diexport ke 'data_pasien.csv")
    except Exception as e:
        print("Error di read table:", e)
    
   # hitung umur otomatis dari tanggal lahir
def get_df(engine):
    df = pd.read_sql("SELECT * FROM pasien_claklinik", engine)

    #parse data
    df["tanggal_lahir"] = pd.to_datetime(df["tanggal_lahir"], errors="coerce")
    df["tanggal_kunjungan"] = pd.to_datetime(df["tanggal_kunjungan"], errors="coerce")

    #umur (turunan)
    today = pd.Timestamp.today()
    df["umur"] = df["tanggal_lahir"].apply(
        lambda x: today.year - x.year - ((today.month, today.day) < (x.month, x.day)) if pd.notnull(x) else None
        )
    return df

def pause ():
    input("\n(Enter untuk lanjut...)")