sayi = int(input("Lütfen sayıyı giriniz: "))

if sayi > 1:
#sayı asal değilse kendinden küçük en az bir sayıya kalansız bölünebilmeli bu yüzden bunun kontrolünü sağladık.

    for i in range(2, sayi,1):
        if(sayi % i) == 0:
            print("Sayı asal değildir.")
            break
    else:
        print("Sayı asaldır.")