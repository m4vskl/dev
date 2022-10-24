num1 = input("Sayı: ")
num2 = input("Sayı: ")
ope = input("Operatörü giriniz:  (+-*/)   ")

islem = num1 + ope + num2
sonuc = eval(islem)
print(sonuc)