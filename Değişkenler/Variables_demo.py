"""
* Bir ogrencinin asagidaki icin gerekli degeskenleri olusturunuz.

Ogrenci adi
Ogernci soyadi
Ogrenci ad + soyad
Ogrenci numarasi
Ogrenci cinsiyet
Ogrenci tc kimlik
Ogrenci dogum yili
Ogrenci adres bilgisi
Ogrenci yasi

"""

ogrenciAdi = 'Git'
ogrenciSoyad = 'hub'
ogrenciAdSoyad = ogrenciAdi + ogrenciSoyad
# ogrenciAdSoyad = ogrenciAdi + ' ' + ogrenciSoyad

print(ogrenciAdSoyad)

ogrenciCinsiyet = True # Erkek
print(ogrenciCinsiyet)

ogrenciCinsiyet = False # Kadın
print(ogrenciCinsiyet)

ogrenciTcKimlik = '12345678900'
ogrenciDogumYili = 2020

ogrenciYas = 2021 - ogrenciDogumYili
print(ogrenciYas)

ogrenciAdres = 'Turkey Istanbul'
print(ogrenciAdres)


"""
* Asagidaki urunlerin toplam bilgisini hesaplayiniz.

Urun 1=> 50     TL
Urun 2=> 60.5   TL
Urun 3=> 356.45 TL

"""
urun1 = 50
urun2 = 60.5
urun3 = 356.45

toplam = urun1 + urun2 + urun3
print("Urun toplam:", toplam)
