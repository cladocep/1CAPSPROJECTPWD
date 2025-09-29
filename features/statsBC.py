import numpy as np
from .read_tableBC import get_df, NUMERIC_COLS

def statistik_umum(engine):
    df = get_df(engine)
    print("\n Kolom numerik:", ",".join(NUMERIC_COLS))
    kolom = input("Pilih kolom: ").strip()
    if kolom not in NUMERIC_COLS:
        print("Tidak valid"); return
    arr = df[kolom].to_numpy()
    print(f"\n Statistik {kolom}:")
    print("Mean:", np.mean(arr))
    print("Median:", np.median(arr))
    print("Std:", np.std(arr))
    print("Min:", np.min(arr))
    print("Max:", np.max(arr))

def statistik_pandas(engine):
    df = get_df(engine)
    print(df[NUMERIC_COLS].describe())

def statistik_biaya(engine):
    df = get_df(engine)
    biaya = df["biaya"].to_numpy()
    print("\n Statistik Biaya:")
    print("Mean:", int(np.mean(biaya)))
    print("Median:", int(np.median(biaya)))
    print("Std:", int(np.std(biaya)))
    print("Min:", int(np.min(biaya)))
    print("Max:", int(np.max(biaya)))
