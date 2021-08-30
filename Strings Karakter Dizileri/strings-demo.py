website = 'https://www.capslockweb.com'
aciklama = 'Biz Yazilimciligi tanitmak ve yaymak icin buradayiz. Gelecekteki nesilleri kafalarinda yazilim nedir ve ne ise yarar gibi sorulari gidermek icin buradayiz.'

# 1- 'aciklama' karakter dizisinde kac karakter bulunmaktadir ?

sonuc = len(website)
sonuc = len(aciklama)


# 2- 'website' icinde www karakterlerini alin.

sonuc = website[8:11]

# 3- 'website' icinde com karakterlerini alin.

karakterSayisi = len(website)
sonuc = website[karakterSayisi-3:karakterSayisi]

# 4- 'aciklama' icinde ilk 15 ve son 15 karakterlerini alin.

sonuc = aciklama[0:16]

# 5- 'aciklama' ifadesindeki karakterleri terstren yazdirin.

sonuc = aciklama[::-1]

# print(sonuc)

# 6- 'Hello world' ifadesinde w harfi 'W' ile degistirin.

s = 'Hello world'
s = s[0:6] + 'W' + s[-4:]

print(s)

# 7- 'abc' ifadesinin yan yana 3 defa yazdirin.

print('abc ' * 3)

name, surname, age, job = 'Git', 'Hub', 20, 'yazilimci'

# 8- Yukaridaki verilen degiskenler ile ekrana asgidaki ifadeyi yazdirin.
#    'Benim adim git Hub, yasim 20 ve meslegim Yazilimci'

sonuc = "Benim adim " + name + " " + surname + ", Yasim " + str(age) + " ve meslegim " + job + "." 
sonuc = "Benim adim {0} {1}, Yasim {2} ve Meslegim {3} ".format(name,surname,age,job)

print(sonuc)