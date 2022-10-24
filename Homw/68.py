# 68-Kullanıcı klavyeden yediği yemeğin ismini yazsın ve ekrana Fiyatı Yazdırılsın 
food = input("yemek: ")
menum = {
    "kahve"     : 15,
    "tavuk dürüm"            : 15,
    "tam ekmek tavuk doner " : 19,
    "Hamburger" : 20,
    "Et dürüm" : 25,
    "Köfte ekmek": 30,
    "Porsiyon köfte": 65,
    "Kahvaltı " : 120,
    "Sigara böreği ": 20,
    }

if food in menum:
    print(menum[food])
else:
    print("Aradığınız kelime Sözlükte bulunamadı")