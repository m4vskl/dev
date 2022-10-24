# 69-Kullanıcı klavyeden yediği yemeklerin  ismini yazsın klavyeden '$' girildiğinde toplam borcu yazdırılsın
food = input("yemek: ")
durum = 1
toplam = 0
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
while durum == 1:
    # girilen yemek menüde var ise dict içindeki karşılığını toplam adlı değişkene int olarak ekle dedik.
    if food in menum:
        print(menum[food])
        toplam += int(menum[food])

    elif food == "$":# $ işareti girildiğinde durum =0 diyerek döngüyü durdurduk ve toplam fiyatı yazdırdık
        print(toplam)
        durum=0

    else:

        print("Aradığınız kelime Sözlükte bulunamadı.")