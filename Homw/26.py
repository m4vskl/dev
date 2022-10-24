import random
deneme = 0
winlose = 0
# random kütüphanesi ile random integer değer çağırdık.
x = random.randint(0,9)
# her seferinde denemeye 1 ekleyerek deneme sayısını saydık.
# tahmin doğru olduğunu break komutu ile döngünün kırılmasını sağladık.

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
