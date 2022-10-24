# 46- ax²+bx+c=0 şeklinde verilen 2. derece denklemin köklerini bul
print("ax²+bx+c şeklindeki denklemin a, b ve c katsayılarını giriniz: ")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
delta = b**2-4*a*c

if delta < 0:
    print("Denklemin reel kökü yoktur.")

elif delta == 0:
    print("Reel kök: ", (-b/2*a))

else:
    print(((-b + delta ** 0.5)/(2*a)), " birinci köktür.")
    print(((-b - delta ** 0.5)/(2*a)), " ikinci köktür.")
