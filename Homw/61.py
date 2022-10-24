# 61-Klavyeden 10 tane tamsayı girilmesini isteyen ve bu girilen tamsayılardan kaç tanesinin negatif kaç tanesinin pozitif olduğunu bul

pozlistem = []
neglistem = []
i = 0

while i < 10:
    num1 = int(input("Sayı giriniz: "))
    i += 1

    if num1 < 0:
        neglistem.append(num1)
    
    elif num1 > 0:
        pozlistem.append(num1)

lpoz = len(pozlistem)
lneg = len(neglistem)

print("Pozitif sayı adedi : ", lpoz)
print("Negatif sayı adedi : ", lneg)