
sayi1 = int(input("İlk sayıyı giriniz: "))
sayi2 = int(input("İkinci sayıyı giriniz: "))

toplam = 0
for i in range(sayi1,sayi2,1):
    if (i%2)==0:
        toplam += i
    
ort = toplam/2
print(ort)
# iki sayı arası çift sayıları bulmak için 2'ye kalansız bölünenleri toplam adlı değişkene ekledik.
