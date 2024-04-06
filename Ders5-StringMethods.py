message="Hello There. My name is Baran Gülmüş"
####################################################################################################################################
        #message = message.upper() #HELLO THERE. MY NAME IS BARAN GÜLMÜŞ <-- Hepsi Büyük.
####################################################################################################################################
        # message = message.lower() #hello there. my name is baran gülmüş <-- Hepsi kücükle baslar.
####################################################################################################################################
        # message = message.title() #Hello There. My Name Is Baran Gülmüş <-- Başlık biciminde, Tüm kelimeler büyükle başlar.
####################################################################################################################################
        # message=message.capitalize() #Hello there. my name is baran gülmüş <-- Baş harfi büyük diğerleri kücük.
####################################################################################################################################
        # message=message.strip() #Hello There. My name is Baran Gülmüş <-- Baştaki BOŞLUĞU Siler.
####################################################################################################################################
        # message=message.split() #['Hello', 'There.', 'My', 'name', 'is', 'Baran', 'Gülmüş'] <-- Boşluklar ile karakterleri ayırarak karakterleri dizeye atar.
####################################################################################################################################
        # message=message.split('.') #[' Hello There', ' My name is Baran Gülmüş'] <-- Nokta(.)'ya göre dizeye atar .
####################################################################################################################################
        # message= " ".join(message) #H e l l o   T h e r e .   M y   n a m e   i s   B a r a n   G ü l m ü ş <-- Itemler arasına boşluk ekler.
####################################################################################################################################
        # index = message.find("Baran")  #24 <-- bu itemin 24. itemden başladıgını söyler.
        # print(index)
####################################################################################################################################
        # message=message.startswith("H") #True <-- Dize 'H' ile mi başlıyor??
####################################################################################################################################
        # message=message.endswith("ş") #True <-- Dize 'ş' ile mi bitiyor??
####################################################################################################################################
        # message=message.replace("Baran", "Samet") # 'Baran' isminde arama yapar ve eğer 'Baran' varsa onu 'Samet' ile değiştir.
        # message=message.replace(" ", "-").replace("ş", "s").replace("ü", "u")
####################################################################################################################################
        # message=message.center(150) #True <-- 150 karakterlik bir container oluştur ve bunun ortasına mesajımızı yaz. 
        # message=message.center(50, "*") #*******Hello There. My name is Baran Gülmüş*******
####################################################################################################################################
print(message)