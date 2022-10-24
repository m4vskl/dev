# 43-while döngüsü ile liste öğlerin ortalamasını hesapla ve ortalamanın yanına listeden kaç eleman olduğunu yazdır 
mylist = [12, 35, 98, 78, 52, 0, 47]

len(mylist)
toplam = 0
i = 0

while i < len(mylist):
    toplam += mylist[i]
    i += 1
    
print(toplam)