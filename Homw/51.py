#  51-Bir fabrikada işçinin alacağı ücret hesaplanırken şu kriterlere uyulmaktadır ; Eğer işçi 40 saatten az çalışmışsa çalıştığı 
#  saat ve saat ücreti çarpılarak alacağı ücret hesaplanıyor , eğer işçi 40 saat ve daha fazla çalışmışsa çalıştığı saat 2 saat
#  olarak hesaplanacak buna göre bilgileri alınarak ödenecek tutarı yazdır 
#  saat başı ücret = 45 TL

forhr= 45
timee = float(input("Kaç saat çalıştınız: "))
salary = 0

if timee < 40:
    salary = (timee * forhr)
    print(salary)

elif timee >= 40:
    extr = (timee-40)*2
    salary = ((timee + extr)* forhr)
    print(salary)