sayilar = [1,3,5,7,9,12,19,21]

# 1-) Sayılar kistesini while ile ekrana yazdırın
        # x=0
        # listeElemanSayisi = len(sayilar)
        # while sayilar:
        #     print(f"Sayılar listesinin {x}. elemanı: {sayilar[x]}")
        #     x+=1
        #     if x == listeElemanSayisi:break;
        # print("bitti")
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////
# 2-) Başlangıc ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıalrı ekrana yazdırın.
        # baslangic=int(input("Başlangıc: "))
        # bitis=int(input("Bitiş: "))
        # for i in range(baslangic,bitis):
        #     if i % 2 == 1:
        #         print(i)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////
# 3-) 1 - 100 arasındaki sasyıları azalan şekilde yazdırın.
        # x=100
        # while x:
        #     print(x)
        #     x-=1
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////
# 3-) Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırınız.
        # x=1
        # sayilarInput=[]
        # while x < 6:
        #     sayilarInput.append(int(input(f"Sayılar listesinin {x}. elemanını giriniz: ")))
        #     x+=1
        # z = 0
        # uzunluk=len(sayilarInput)
        # sayilarInput.sort()
        # while sayilarInput:
        #     print(sayilarInput[z])
        #     z+=1
        #     if uzunluk == z:break
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////
# 4-) Kullanıcıdan alacağınız sınırsız ürün bilgisini ürünler listesi icinde saklayınız:
#    **ürün sayısını kullanıcıya sorun.
#    **dictionary liste yapısı (name, price) şeklinde olsun.
        # urunler=[]
        # urunSayisi = int(input("Ürün Sayısı: "))
        # i = 0
        # while i<urunSayisi:
        #     name = input(f"{i}. ürün ismi: ")
        #     price = input(f"{i}. ürün fiyatı: ")
        #     urunler.append(
        #         {
        #             "name": name,
        #             "price": price
        #         }
        #     )
        #     i += 1
        # for urun in urunler:
        #     print(f"ürün adı: {urun['name']} / ürün fiyatı: {urun['price']}")