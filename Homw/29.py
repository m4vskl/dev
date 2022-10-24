txt = """The Nords are the race of men native to Skyrim. Nords consider themselves to be the Children of the Sky. They call Skyrim the Throat of the World because it was
where the sky first brought the North Winds upon land and formed them. Breath and the voice are the vital essences of a Nord; the art of breathing, speech and articulation
is with them. Though the art of speech is usually associated with the goddess Dibella, the art of the Thu'um, or Storm Voice, is associated with Kynareth, who gave Men
the ability to speak."""

soru = input("Aramak istediğiniz metni girin: ")
x = txt.find(soru)

# eğer x 0'dan başlayarak bir index değeri veremiyorsa bu metnin dosyada olmadığı anlamına gelir.
if x == -1:
    print("Aradığınız metin bu dosyada yok.")
else:
    print("Aradığınız metin bu dosyada var.")

