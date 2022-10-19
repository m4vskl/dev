kiloo = int(input("Lütfen kilonuzu giriniz: "))
boy= int(input("Lütfen cm cinsinden boyunuzu giriniz: "))
boym = boy/100 
# Kullanıcı metre cinsinden girdiğinde nokta yerine virgül kullanıp karışıklığa sebep olabilir. bu yüzden cm cinsinden
# değeri alıp programın metreye çevirmesini sağladık.

vki = ((kiloo)/(boym**2))
print("Vücut kitle indeksiniz: ", vki)