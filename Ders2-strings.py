name="Baran"
surname = "Gülmüş"
age=16
selam="hi, my name is " + name + " "+ surname + ", i am " + str(age) + " years old."
print(selam)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
selamLenght=len(selam)
print("selam uzunluğu: " , selamLenght)
print("selamın 5. itemi: " , selam[5])
print("selamın sonuncu itemi: " , selam[-1])
print("selamın 0 den 5 e kadar olan itemi: " , selam[0:5])
print("selamın 15 den sonraki itemleri: " , selam[15:])
print("selamın 20 den önceki itemleri: " , selam[:20])
print("selamın 0 dan sonuncu iteme kadar olanları al ama iki karakterden birini al: " , selam[0:-1:2])