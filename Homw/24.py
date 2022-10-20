maas = int(input("Maaşınızı giriniz: "))
zamcik = int(input("Zam oranını yüzde olarak giriniz: "))

maas2 = ((maas*zamcik)/100)+ maas
print("Yeni maaşınız: ", maas2)