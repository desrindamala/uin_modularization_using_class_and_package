name = 'desrinda mala'
program = 'apa yang merasukimu'

print (f' program {program} oleh {name}')

def hitung_perubahanEntropi (kalor, suhu):
    perubahanEntropi = kalor / suhu
    print (f' kalor  {kalor / 2000} joule pada suhu = {suhu / 300} Kelvin')
    print (f' sehingga perubahan entropi = { perubahanEntropi } J/K')
    return kalor/suhu
# kalor = 2000
# suhu = 300
perubahanEntropi = hitung_perubahanEntropi (2000, 300)

def hitung_energiPotensial (  massa, gravitasi, tinggi ):
    energiPotensial = massa * gravitasi * tinggi
    print (f'massa benda {massa  / 100} kg dengan {gravitasi / 9.98} m/s {tinggi / 50} m')
    print (f' sehingga energi potensial = { energiPotensial} J')
    return massa  * gravitasi * tinggi
# massa = 100
# gravitasi = 9.98
# tinggi = 50
energiPotensial = hitung_energiPotensial (100, 9.98, 50)

def hitung_bedaPotensial ( arus , hambatan):
    bedaPotensial = arus * hambatan
    print (f' kuat arus { arus / 13} A dengan {hambatan / 2.2} ohm')
    print (f' sehingga beda potensial = {bedaPotensial} V')
    return  arus * hambatan
# arus = 13
# hambatan 2.2
bedaPotensial = hitung_bedaPotensial ( 13, 2.2)




