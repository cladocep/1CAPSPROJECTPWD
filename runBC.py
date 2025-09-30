from db.connectionBC import buat_koneksi
from features.read_tableBC import read_table, NUMERIC_COLS
from features.statsBC import statistik_umum, statistik_pandas, statistik_biaya
from features.visualizeBC import viz_kategorikal, viz_numerik, viz_produk, viz_biaya, viz_pasien_per_bulan
from features.crudBC import tambah_pasien, update_pasien, hapus_pasien
from features.searchBC import cari_data
from features.recommendBC import rekomendasi
from features.Matrix_korelasi import plot_correlation_heatmap
from utils.helpersBC import pause

def main():
    engine = buat_koneksi()
    if not engine:
        return
    
    try:
        while True:
            print("\n=== MENU UTAMA ===")
            print("1. Read Data / Tampilkan data (+Export CSV)")
            print("2. Statistik umum")
            print("3. Statistik describe")
            print("4. Statistik biaya")
            print("5. Visualisasi kategorikal")
            print("6. Visualisasi numerik")
            print("7. Visualisasi produk skincare")
            print("8. Visualisasi biaya")
            print("9. Visualisasi pasien perbulan")
            print("10. Tambah pasien")
            print("11. Update Pasien")
            print("12. Hapus pasien")
            print("13. Cari data")
            print("14. Rekomendasi layanan")
            print("15. Matrix Korelasi Data Pasien")
            print("0. Keluar")
            
            
            pilihan = input("Masukkan pilihan Anda (1-15): ")
            
            if pilihan == "1":
                print(read_table(engine)); pause()
            elif pilihan == "2":
                statistik_umum(engine);pause()
            elif pilihan == "3":
                statistik_pandas(engine);pause()
            elif pilihan == "4":
                statistik_biaya(engine);pause()
            elif pilihan == "5":
                viz_kategorikal(engine);pause()
            elif pilihan == "6":
                viz_numerik(engine);pause()
            elif pilihan == "7":
                viz_produk(engine);pause()
            elif pilihan == "8":
                viz_biaya(engine);pause()
            elif pilihan == "9":
                viz_pasien_per_bulan(engine);pause()
            elif pilihan == "10":
                tambah_pasien(engine);pause()
            elif pilihan == "11":
                update_pasien(engine);pause()
            elif pilihan == "12":
                hapus_pasien(engine);pause()
            elif pilihan == "13":
                cari_data(engine);pause()
            elif pilihan == "14":
                rekomendasi();pause()
            elif pilihan == "15":
                plot_correlation_heatmap(engine);pause()
            elif pilihan == "0":
                print("Terimakasih telah menggunakan applikasi ini");break
                
    finally:
        # Menutup koneksi database
        engine.dispose()
        print("Koneksi database ditutup")

if __name__ == "__main__":
    main()