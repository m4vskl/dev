# 52- Klavyeden girilen 10 sayıyı toplayan ve sonucu ekranda göster
listem = []
durum = 0
toplam = 0
while durum < 10:
    num1 = int(input("Sayıyı giriniz: "))
    listem.append(num1)
    durum += 1

for i in listem:
    toplam += i
ort = toplam/10
print (ort)