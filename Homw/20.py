# Kullanıcıdan iki tane sayı aldık.

sayi1 = int(input("Birinci sayıyı giriniz: "))
sayi2 = int(input("İkinci sayıyı giriniz: "))
toplam = 0
# sayi1 ve sayi2 arasındaki bütün değerleri toplam değişkenine eşitleyerek toplamaya devam ettik.
for x in range (sayi1, sayi2, 1):
    toplam = x+toplam
    print (toplam)
