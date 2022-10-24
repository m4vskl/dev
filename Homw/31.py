# tek sayılar ve çift sayılar için ayrı ayrı liste oluşturduk.
tekler = []
ciftler = []

durum= 1
# kullanıcı q yazana kadar while içerisindeki sayı alma durumunun devam etmesini sağladık.
while durum == 1:
    
    a = int(input("Sayıyı giriniz: "))
    # çift sayıları çift listesine, tek sayıları tek listesine ekledik.
    if (a %2)==0:
        ciftler.append(a)
    else:
        tekler.append(a)
    print(tekler)
    print(ciftler)
    
    quitt = input("Çıkmak için q yazın yada boş geçin: ")
    if quitt == "q":
        break

#tekler listesinin ortalamasını aldık.
tekler_ort = (sum(tekler)) / 2
print(tekler_ort)
# çiftler listesinin ortalamasını aldık.
ciftler_ort = (sum(ciftler)) / 2
print(ciftler_ort)