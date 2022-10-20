sayi1 = int(input("Birinci sayıyı giriniz: "))
sayi2 = int(input("İkinci sayıyı giriniz: "))
toplam = 0
for x in range (sayi1, sayi2, 1):
    toplam = x+toplam
    print (toplam)
