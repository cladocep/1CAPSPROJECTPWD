def rekomendasi():
    umur = int(input("Umur Pasien : "))
    if umur < 25:
        print("Rekomendasi  Acne Treatment + Paket Acne Skincare")
    elif umur < 40:
        print("Rekomendasi: Facial/Laser + Paket Brightening Skincare")
    else:
        print("Rekomendasi: Botox/Filler +Anti-Aging Skincare")