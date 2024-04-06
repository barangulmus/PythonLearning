website = "https://www.sadikturan.com"
course = " Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 Saat)  "
# 1- 'Hellow World' karakter dizisinin baş ve son boşluk karakterlerini silin.
    # characters="        Hello World "
    # DelToCharacters = characters.strip()
    # DelToCharacters = characters.lstrip('/:tph') <-- left taraftan başlayarak '/,:,t,p,h' karakterlerini siler
    # print(DelToCharacters)
######################################################################################
# 2- website icindeki 'sadikturan' haric tüm karakterleri silin.
    # site = website
    # DelSite = website[12:]
    # print(DelSite[:-4])
######################################################################################
# 3 - course dizesinin tüm karakterlerini kücük harf yapın
    # print(course.lower())
######################################################################################
# 4 - website icerisinde kac tane a karakteri vardır?
    # print(website.count("a"))
######################################################################################
# 5 - website www ile başlayıp com ile bitiyor mu?
    # print("www ile başlıyor mu? ",website.startswith("www"))
    # print("com ile bitiyor mu? ",website.endswith("com"))
######################################################################################
# 6 - website dizenin icerisinde '.com' ifadesini iceriyor mu?
    # print(website.find(".com"))
######################################################################################
# 7 - course icindeki karakterlerin hepsi alfabetik mi?
    # print(website.isalpha())
######################################################################################
# 8 - 'Contents' ifadesini satırda 50 karakter icinde yerleştirip sağ ve soluna * ekleyiniz
    # print("Contents".center(50, "*"))
######################################################################################
# 9 - course karakter dizesindeki tüm boşluk karakterlerini '-' ile değiştirin.
    # print(course.replace(" ", "-"))
######################################################################################
# 10 - 'Hellow World' ifadesi icerisindeki 'Hello' ifadesini 'There' olarak değiştirin.
    # print("Hello World".replace("Hello", "There"))
######################################################################################
# 11 - course karakter dizesini boşlık karakterlerinden ayırı.
    # print(course.split(" "))