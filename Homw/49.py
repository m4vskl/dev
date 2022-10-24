# 49- Klavyeden girilen bir sayının pozitif ya da nagatif olduğunu ekrana yazdır

num1 = float(input("Sayıyı giriniz: "))

if num1 > 0:
    print("Sayı pozitif ")

elif num1 == 0:
    print("Sayı sıfırdır.")
    
elif num1 < 0:
    print("Sayı negatif")