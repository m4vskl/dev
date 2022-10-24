sayi1 = int(input("Kaça kadar çift sayıları toplamak istiyorsunuz: "))
x = 0
toplam0 = 0
toplam1 = 0
# çift sayıları için 0'dan başlayıp ikişer artarak devam eden bir sayı kümesi yazdık. Bu sayı kümesi kullanıcıdan aldğımız sayıya 
# kadar ikişer artarak devam edecek.
while x < sayi1:
    x = x+2
    toplam0 = toplam0+x
    print (toplam0)

sayi2 = int(input("Kaça kadar tek sayıları toplamak istiyorsunuz: "))
# tek sayılar için -1'den başlayıp ikişer artarak devam eden bir sayı kümesi yazdık.
x = -1
while x < sayi2:
    x = x+2
    toplam1 = toplam1+x
    print (toplam1)