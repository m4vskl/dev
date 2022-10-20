x1 = int(input("Birincin noktanın x değeri: "))
y1 = int(input("Birincin noktanın y değeri: "))

x2 = int(input("İkinci noktanın x değeri: "))
y2 = int(input("İkinci noktanın y değeri: "))

def koordinat(x1,y1,x2,y2):
    uzaklik = ((x2-x1)**2 + (y2-y1)**2)**1/2
    print("İki nokta arası uzaklık: ", uzaklik)

koordinat(x1,y1,x2,y2)