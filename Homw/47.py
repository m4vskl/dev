# 47-Bir ürünü alış fiyatı üzerinden klavyeden vergi oranı(%18 KDV) ve kar oranı eklenerek satış fiyatına hesapla
prodc = 98
print("Ürünün alış fiyatı 98 TL'dir.")

tax = float(input("Vergi oranı: "))

taxp = (prodc*tax)/100
prodc = taxp + prodc
profit = float(input(("Yüzde kaç kar etmek istiyorsunuz: ")))

profitp = (prodc*profit)/100
prodc = profitp + prodc
print(prodc)