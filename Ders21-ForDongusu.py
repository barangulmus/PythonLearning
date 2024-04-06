# numbers = [1, 2, 3, 4, 5]
# for x in numbers:
#     print(x)
###########################################
# x = {"k1":1, "k2":2, "k3":3}
# for key,value in x.items():
#     print(key,value)
    
sayilar = [1, 3, 5, 7, 9, 12, 19, 21]
# 1 - Sayılar listesindeki hangi sayılar 3'ün katıdır?
    # for sayi in sayilar:
    #     if sayi % 3 == 0:
    #         print(sayi)
# 2 - Sayılar listesindeki sayıların toplamı kactır?
        # print(f"Sayılar dizesindeki sayıların toplamı: {sum(sayilar)}")
    # toplam = 0
    # for x in sayilar:
    #     toplam += x
    # print(toplam)
# 3 - Sauılar listesindeki tek sayıların karesini alınız.
    # for i in sayilar:
    #     print(f"{i}'nin karesi ==> {i**2}");
#  4 - Şehirlerden hangileri en fazla 5 karakterlidir?
    # sehirler = ["Kocaeli", "İstanbul", "Ankara", "İzmir", "Rize"]
    # for r in sehirler:
    #     if len(r) < 6:
    #         print(r)

urunler = [
    {"Name": "Samsung Galaxy s6", "price":3000},
    {"Name": "Samsung Galaxy s7", "price":4000},
    {"Name": "Samsung Galaxy s8", "price":5000}, 
    {"Name": "Samsung Galaxy s9", "price":6000},
    {"Name": "Samsung Galaxy s10", "price":7000},
]
#  5 - urunlerin fiyat toplamı nedir
    # toplam = 0
    # for ğ in urunler:
    #     toplam = toplam + ğ["price"]
    # print(toplam)
# 6 - ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz
for u in urunler:
    if u["price"] < 5001:
        print(u["Name"],"===>", u["price"])