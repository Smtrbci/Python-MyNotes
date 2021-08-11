website = "http://www.monster.com.tr"
course  = "Türkiyenin en kaliteli bilgisayar : Monster"

# 1- 'course' karakter dizisinde kaç karekter bulunamktadır ?

result = len(course)
length = len(website)

# 2- 'websitesi' içinden www karakterlerini alın.

result = website[7:10]

# 3- 'websitesi' içinden com karakterlerini alın.

result = website[19:22]
result = website[length-2:length]

# 4- 'course' içinden ilk 15 ve son 15 karakterlerini alın.

result = course[0:33]

# 5- 'course' ifadesindeki karakterleri tersten yazdırın 

result = course[::]
s = '12345' * 5
print(s[::])

name , surname , age , job = 'Samet','Arabacı', 20, 'Yazılım'

# 6- Yukarıda verien değişkenlerd ise ekrana aşağıdaki ifadeyi yazın.
#     'Benim adım Samet Arabacı, Yaşım 20 ve maesleğim yazılım.'

result = "Benim adım "+ name+ " " + surname+ ", Yaşım "+ str(age) + " ve masleğim " + job

#7- 'Hello word' ifadesindeki w harfini 'W' ile değiştirin.

s = 'Hello world'
result = s[6]

#8- 'abc' ifadesini yan yan 3 defa yazdırın.

result = 'abc ' * 3

print(result)
