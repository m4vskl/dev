# Sinema 49.5 TL
# Tiyatro 29.8 TL
sinema = 49.5
tiyatro = 29.8
fiyat = 0
ind = 0
ind_durum = input("Öğrenci misiniz ? EVET/HAYIR \n ")
if ind_durum == "EVET":
    print("%50 indirimden faydalanabilirsiniz.")
    ind = 0.5
elif ind_durum == "HAYIR":
    ind = 1
else:
    quit()
    

bilet = int(input("Sinema bileti almak için 1, tiyatro bileti için 2 yazınız."))

if bilet == 1:
    fiyat = sinema*ind
    print("Ödemeniz gereken fiyat: ", fiyat)

elif bilet == 2:
    fiyat = tiyatro*ind
    print("Ödemeniz gereken fiyat: ", fiyat)
    
