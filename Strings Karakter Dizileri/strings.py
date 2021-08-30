ad = 'Git'
soyad = 'hub'
yas = '20'

msj = 'Benim adim ' + ad + ' ve soyadim ' + soyad + '.Yasim ise ' + yas + '.'
KarakterSayisi = len(msj)

print(msj[0])
print(msj[1])
print(msj[-1])
print(msj[KarakterSayisi - 1])

print(msj[0:5])
print(msj[6:16])
print(msj[:10])
print(msj[10:])

print(msj[-10:-1])
print(msj[0:40:2])
print(msj[::1])
print(msj[::-1])