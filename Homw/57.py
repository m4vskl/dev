# 57-1+4+9+ … +100= değerini hesapla
# 1'den 10'a kadar olan sayıların karesini toplamamızı istediği için x adlı değişkeni her seferinde bir arttırarak karesini aldık
# ve toplam adlı değişkene ekledik.
x = 1
toplam = 0
while x <= 10:
    sqr = x**2
    toplam += sqr
    x += 1

print(toplam)
