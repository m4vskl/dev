import random
deneme = 0
winlose = 0

x = random.randint(0,9)

while winlose == 0:
    soru = int(input("Tahmininiz: "))
    if soru == x:
        print("Doğru bildiniz.")
        deneme += 1
        print(deneme, "kez denedikten sonra sonuca ulaştınız.")
        break
    else:
        deneme += 1
        continue
