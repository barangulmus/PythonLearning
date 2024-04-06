# key - value
sehirler = ["Kocaeli", "Istanbul"]
# plakalar = [41, 34]
# print(plakalar[sehirler.index("Kocaeli")])   )=> 41
# print(plakalar[sehirler.index("Istanbul")])   )=> 34

plakalar = {
    "Kocaeli":41,
    "Istanbul":34
}
users={
    "barangulmus" : 
    {
        "adi" : "Baran",
        "soyadi" : "Gülmüş",
        "yasi" : 16
    },
    "administator" : 500
}
print(users["barangulmus"]["adi"])