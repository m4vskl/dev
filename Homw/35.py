import datetime

#datetime kütüphanesi ile elde ettiğimiz bugünün yılını girilen yıldan çıkararak yaş hesabı yaptık.
dogumy = int(input("Doğum yılınızı giriniz: "))
guncel_tarih = datetime.datetime.now()
guncel_yil = guncel_tarih.year

yas = guncel_yil-dogumy

print(yas)
