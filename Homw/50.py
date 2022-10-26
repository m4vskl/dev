# 50-Bir fabrikada sabit maaşla çalışan işçiler aile durumlarına göre ek maaş almaktadırlr. 
# Çocuk sayısı 1 ise maaşının %5’i kadar , çocuk sayısı 2 ise %10’u 3 ve daha fazla ise %15’i kadar aile yardımı almaktadır. 
# Buna göre kullanıcıdan işçinin maaşı ve çocuk sayısı istenerek gerekli hesaplamayı yap

salary = float(input("Maaş tutarı: "))
kid = float(input("Çocuk sayısı: "))

extra = (salary*(kid*5))/100 # çocuk yardımı miktarı
salaryn = extra + salary
print(salaryn)