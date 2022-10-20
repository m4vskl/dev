sayi = int(input("Lütfen sayıyı giriniz: "))

if sayi > 1:

    for i in range(2, sayi,1):
        if(sayi % i) == 0:
            print("Sayı asal değildir.")
            break
    else:
        print("Sayı asaldır.")