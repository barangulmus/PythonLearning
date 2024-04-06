#  1 - Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
        # sayi = int(input("sayi: "))
        # if sayi <= 100 and sayi >= 0:
        #     print("sayı 0 ile 100 arasındadır.")
        # else:
        #     print("sayi 0 ile 100 arasında değildir.")
####################################################################################################
#  2 - Girilen bir sayının pozitif sayı olup olmadıgını kontrol ediniz.
        # sayi=int(input("sayi: "))
        # if sayi > 0 and sayi % 2 == 0:
        #     print("Sayınız pozitif bir cift sayıdır.")
        # else:
        #     print("Sayınız pozitif bir cift sayı değildir.")
####################################################################################################
#  3 - Email ve parola bilgileri ile giriş kontrolü yapınız.
        # email=str(input("Enter your email address: "))
        # password=str(input("Enter your password: "))
        # if email == "barangulmus@gmail.com" and password == "abs123":
        #     print("Login succsess")
        # else:
        #     print("Login unsusccsess")
####################################################################################################
#  4 - Girilen 3 satıtı büyüklük olarak karşılaştırınız.
        # x=int(input("1 : "))
        # y=int(input("2 : "))
        # z=int(input("3 : "))
        # dizi = [x, y, z]
        # dizi.sort()
        # m = dizi[::-1]
        # for l in m:
        #     print(l, ">",end=" ")
####################################################################################################
#  5 - Kişinin ad, kilo ve boy bilgilerini alıp kilo indexlerini hesaplayınız.
#  Formül: (Kilo / boy uzunluğunun karesi)
#  Aşağıdaki gruba göre kişi hangi tabloya girmektedir??
#    0 - 18.4 => Zayıf
#    18.5 - 24.9 => Normal
#    25.0 - 29.9 => Fazla Kilolu
#    30.0 - 34.9 => Obez
ad = str(input("Ad: "))
kilo = float(input("Kilo: "))
boy = float(input("Boy: "))
index = kilo / boy**2

if index > 0 and index < 18.5:
    print(f"{ad}, Zayıfsın.")
elif index >= 18.5 and index < 25:
    print(f"{ad}, Normalsin.")
elif index >= 25 and index < 30:
    print(f"{ad}, Fazla Kilolusun.")
elif index >= 30 and index < 35:
    print(f"{ad}, Obezsin.")
else:
    print(f"{ad}, Allah Rahmet Eğlesin.")
####################################################################################################