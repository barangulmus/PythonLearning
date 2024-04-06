x, y, z = 2, 5, 107
numbers = 1, 5, 7, 10, 6
# 1 - Kullanıcıdan aldığınız 2 sayının carpımı ile x, y, z toplamının farkı nedir?
# sayi1=int(input("Birinci sayıyı giriniz: "))
# sayi2=int(input("İkinci sayıyı giriniz: "))
# carpim = sayi1 * sayi2
# toplam = (x + y + z) + carpim
# print(toplam)
#################################################################################
# 2 - y'nin x'e kalansız bölümünü hesaplayınız.
# a = y // x
# print(a)
#################################################################################
# 3 - (x,y,z) toplamının mod'ü kactır?
# mod3 = (x + y + z) % 3
# print(mod3)
#################################################################################
# 4 - y'nin x. kuvvetini hesaplayınız.
# print(y**x)
#################################################################################
# 5 - x, *y, z = numbers işlemine göre z'nin küpü kactır?
# x, *y, z = numbers
# print(z ** 3)
#################################################################################
# 6 - X, *Y, Z = NUMBERS işlemine göre Y'nin değerleri toplamı kactır?
x, *y, z = numbers
a = y[0] + y[1] +y[2]
print(a)