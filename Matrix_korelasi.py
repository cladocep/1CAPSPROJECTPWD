import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def get_df(engine):
    try:
        with engine.connect() as conn:
            df = pd.read_sql("SELECT * FROM pasien_claklinik", conn)
            print(df)
        return df
    except Exception as e:
        print("Error di read table:", e)
        return pd.DataFrame()
  
def plot_correlation_heatmap(engine):
    df = get_df(engine)
    
    #buang kolom bukan angka
    drop_cols = ["id_pasien", "nama_pasien", "jenis_kelamin", "layanan"]
    df = df.drop(columns=[c for c in drop_cols if c in df.columns], errors="ignore")

    #push kolom jadi numerik, yang tidak bisa =NaN
    numeric_df = df.apply(pd.to_numeric, errors="coerce")

    #hapus kolom yang ful NaN
    numeric_df = numeric_df.dropna(axis=1, how="all")

    # print korelasi ke terminal
    print("\n== Matrix Korelasi Data Paien")
    corr_matrix =numeric_df.corr()
    print(corr_matrix)

    print("\nKeterangan Korelasi:")
    print("- Nilai mendekati +1 artinya hubungannya kuat dan searah.")
    print("- Nilai mendekati -1 artinya hubungannya kuat tapi berlawanan arah.")
    print("- Nilai mendekati 0 artinya hampir tidak ada hubungan.")

    #Interpretasi ototamatis tanpa duplikasi
    print("\nInterpretasi otomatis:")
    checked = set()
    for col1 in corr_matrix.columns:
        for col2 in corr_matrix.columns:
            if col1 !=col2 and (col2,col1) not in checked:
                val = corr_matrix.loc[col1, col2]
                hubungan ="positif" if val > 0 else "negatif" if val < 0 else "tidak ada hubungannya"
                print(f"- {col1} dengan {col2}: {val:.2f} ({hubungan})")
                checked.add((col1, col2))
    # Heatmap
    plt.figure(figsize=(12,10))
    sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", fmt=".2f", square=True, cbar_kws={"shrink": 0.5})
    plt.title("Matrix Korelasi Data Pasien",pad=20)
    plt.xticks(rotation=45, ha="right")
    plt.yticks(rotation=0)
    plt.tight_layout()
    plt.subplots_adjust(bottom=0.25)
    plt.show()
