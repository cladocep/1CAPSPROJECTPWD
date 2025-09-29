import seaborn as sns
import matplotlib.pyplot as plt
from .read_tableBC import get_df, NUMERIC_COLS, CATEG_COLS

def viz_kategorikal(engine):
    df = get_df(engine)
    kolom = input(f"Pilih kolom kategorikal {CATEG_COLS}: ").strip()
    if kolom not in CATEG_COLS:
        print("Tidak valid"); return
    sns.countplot(x=kolom, data=df)
    plt.title(f"Distribusi {kolom}")
    plt.show()

def viz_numerik(engine):
    df = get_df(engine)
    kolom = input(f"Pilih kolom numerik {NUMERIC_COLS}: ").strip()
    if kolom not in NUMERIC_COLS:
        print("Tidak Valid"); return
    sns.histplot(df[kolom], kde=True, bins=10)
    plt.title(f"Distribusi {kolom}")
    plt.show()
    sns.boxplot(y=df[kolom])
    plt.title(f"Boxplot {kolom}")
    plt.show()

def viz_produk(engine):
    df = get_df(engine)
    g = df.groupby("layanan")["produk_skincare"].mean().reset_index()
    sns.barplot(x="layanan", y="produk_skincare", data=g)
    plt.title("Rata-rata Produk Skincare per Layanan")
    plt.show()

def viz_biaya(engine):
    df = get_df(engine)
    plt.subplot(1,2,1)
    sns.histplot(df["biaya"], kde=True, bins=10)
    plt.title("Distribusi Biaya")
    plt.subplot(1,2,2)
    sns.boxplot(y=df["biaya"])
    plt.title("Boxplot Biaya")
    plt.tight_layout()
    plt.show()

def viz_pasien_per_bulan(engine):
    df = get_df(engine)
    df["bulan"] = df["tanggal_kunjungan"].dt.to_period("M")
    count = df.groupby("bulan")["id_pasien"].count()

    count.plot(kind="bar")
    plt.title("Jumlah Pasien per Bulan")
    plt.xlabel("Bulan")
    plt.ylabel("Jumlah Pasien")
    plt.show()