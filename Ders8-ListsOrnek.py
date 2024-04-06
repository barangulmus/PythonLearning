# 1 - "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.
liste = ["BMW","Mercedes","Opel","Tesla"]
# 2 - Liste Kaç elemanlıdır ?
    # kacElemanVar=len(liste)
    # print(kacElemanVar)
# 3 - Listenin ilk ve son elemanı nedir?
    # ilkEleman = liste[0]
    # sonEleman = liste[-1]
    # print(f"İlk Eleman: {ilkEleman}\nSon Eleman: {sonEleman}")
# 4 - Opel değerini Toyota ile değiştirin.
    # degistir=liste[2]="Toyota"
    # print(liste)
# 5 - Mercedes listenin bir elemanı mıdır?
    # print(liste.count("Mercedes"))
    # print('Mercedes' in liste)
# 6 - Listenin -2 indeksindeki değer nedir ?
    # print(liste[-2])
# 7 - Listenin ilk 3 elemanını alın.
    # print(liste[:3])
# 8 - Listenin son 2 elemanı yerine "Totoya" ve "Renault" değerlerini ekleyin.
    # degistir1=liste[-2]="Toyota"
    # degistir=liste[-1]="Renault"
    # print(liste)
# 9 - Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.
    # liste.append("Audi")
    # liste.append("Nissan")
    # print(liste)
# 10 - Listenin son elemanını silin.
    # liste.remove(liste[-1])
    # print(liste)
# 11 - Liste elemanlarını tersten yazdırınız.
    # print(liste[::-1])
# 12 - Aşağıdaki verileri bir liste içinde saklayınız.
studentA=["Yiğit","Bilgi",2010,[70,60,70]]
studentB=["Sena","Turan",2010,[80,80,70]]
studentC=["Ahmet","Turan",2010,[80,70,90]]
# studentA: Yiğit Bilgi 2010, (70,60,70)
# studentB: Sena Turan 1999, (80,80,70)
#studentC: Ahmet Turan 1998, (80,70,90)
print(studentA[3][1])