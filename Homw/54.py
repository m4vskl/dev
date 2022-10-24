listem = []

num1 = int(input("Birinci sayıyı giriniz: "))
num2 = int(input("İkinci sayıyı giriniz: "))
num3 = int(input("Üçüncü sayıyı giriniz: "))

listem.append(num1)
listem.append(num2)
listem.append(num3)

listem.sort()

print(listem[0])
print(listem[2])