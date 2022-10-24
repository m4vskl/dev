# 65-Bir Lokanta olsun bu lokantanın menüsü bir dictionary de tutulsun ve ekrana tüm menü yazdırılsın (Yemek İsmi ve Fiyatı)
menum = {
    "soslu tavuk doner"     : 15,
    "tavuk dürüm"            : 15,
    "tam ekmek tavuk doner " : 19,
    "Hamburger" : 20,
    "Et dürüm" : 25,
    "Köfte ekmek": 30,
    "Porsiyon köfte": 65,
    "Kahvaltı " : 120,
    "Sigara böreği ": 20,
    }

for key, value in menum.items():
  print(key, ": ", value)
