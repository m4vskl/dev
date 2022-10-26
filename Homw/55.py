

num1 = int(input("Birinci sayıyı giriniz: "))
num2 = int(input("İkinci sayıyı giriniz: "))
# sayılardan birincisinin büyük olmasını istiyoruz. eğer küçük ise diğer değişkenle değiştirmesini sağladık

if num1 < num2:
    num1 , num2 = num2, num1

for i in range(num2,num1,1):
    print(i)
