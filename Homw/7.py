vize = int(input("Lütfen vize notunu giriniz: "))
finalnot = int(input("Lütfen final notunu giriniz: "))
ort = (vize*0.4) + (finalnot*0.6) #vize genel notun %40, final %60'ı olacak şekilde hesaplanmıştır.

print("ortalamanız: ",ort)

if 100 > ort >= 45:
    print("GEÇTİNİZ. ")

elif 0 < ort < 45:
    print("KALDINIZ:")

else:
    print("Geçersiz not girdiniz.")
    