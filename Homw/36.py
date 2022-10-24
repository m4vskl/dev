import datetime
# kullanıcıdan ayrı ayrı gün/ ay/ sayılarını integer olarak aldık.
dogumg= int(input("Doğum gününüzü giriniz: "))
doguma= int(input("Doğum ayınızı giriniz: "))
dogumy= int(input("Doğum yılınızı giriniz: "))
#aldığımız sayıları datetime ile dogumt adında bir değişkene tarih formatı vererek ekledik.
dogumt = datetime.datetime(dogumy,doguma,dogumg)

print("Doğduğunuz gün: ", dogumt.strftime("%A")) # dogumt tarihindeki haftanın gününü bulduk.
bugun = datetime.datetime.today()
buyil = bugun.year
# bugün içinde bulunduğumuz yılı buyil adlı değişkene attık.

while buyil > dogumy:
    # günümüze gelene kadar doğum tarihindeki yıl kısmına bir yıl ekleyerek her yıl için haftanın hangi gününe
    #  geldiğini hesapladık ve yazdırdık
    dogumy = dogumy+1
    dogumtt = datetime.datetime(dogumy,doguma,dogumg)
    print(dogumtt.strftime("%A"))