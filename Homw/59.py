# 59-Klavyeden ardı ardına girilen sayıları toplayan ve girilen sayı negatif olduğunda durup ortalamayı hesapla
num1 = 0
durum = 1
toplam = 0
sayac = 0
while durum == 1:
    num1 = int(input("Sayıyı giriniz: "))
    toplam += num1
    if num1 >= 0:
        sayac += 1
        continue
    else:
        durum = 0
        sayac -= 1

ort = (toplam/sayac)

print(ort)

