ogrenciler={}
for i in range(1,2):
    ad = str(input(f"{i}. Öğrencinin adını giriniz: "))
    soyad = str(input(f"{i}. Öğrencinin soyadını giriniz: "))
    okulNo = int(input(f"{i}. Öğrencinin okul numarasını giriniz: "))
    tel = str(input(f"{i}. Öğrencinin telefon numarasını giriniz: "))
    ogrenciler[okulNo] = {
        "ad":ad,
        "soyad":soyad,
        "tel":tel
    }
    print("///////////////////////////////////////////////////////////")
    if i == 1 :
        a = int(input("Okul numaranızı giriniz: "))
        c = ogrenciler[a]
        print(f"Merhaba {c['ad']} {c['soyad']}, şuan listeyi görüntülemektesiniz. Bize {c['tel']} numaranızdan ulaşabilirsiniz.")