
prodc = 98
print("Ürünün alış fiyatı 98 TL'dir.")

tax = float(input("Vergi oranı: "))

taxp = (prodc*tax)/100 # üründeki vergi miktarı
prodc = taxp + prodc
profit = float(input(("Yüzde kaç kar etmek istiyorsunuz: ")))

profitp = (prodc*profit)/100 # üründeki kar miktarı
prodc = profitp + prodc
print(prodc)