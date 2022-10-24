durum =1
toplam = 0

while durum == 1:
    sayi1 = int(input("Sayıyı giriniz: "))
    toplam += sayi1
    print(toplam)
    if sayi1 == 0:
        durum = 0
        break
