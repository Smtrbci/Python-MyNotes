# 1-  "Bmw, Mercedes,Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.

arabalar = ['Bmw','Mercedes','Opel','Mazda']

# 2-  Liste kaç elemanlıdır ?

result = len(arabalar)

# 3-  Lİstenin ilk ve son elemanı nedir ?

result = arabalar[0]
result =arabalar[3]
result = arabalar[-1]
result = arabalar[-2]

# 4-  Mazda değerini Toyota ile değiştin.

arabalar[-1]='Toyota'
result = arabalar 

# 5-  Mercedes listenin bir elemanı mıdır ?

result = 'Mercedes' in arabalar

# 6-  Listenin -2 indeksindeki alın.

result = arabalar[-2]

# 7-  Listenin ilk 3 elemanın alın.

result = arabalar[0:3]
result = arabalar[:3]
result = arabalar[-2:]

# 8-  Listenin son 2 elemanın yerine "Toyoto" ve "Renault" değerlerini ekleyin.

arabalar[-2:] = ['Toyota','Renault']
result = arabalar

# 9-  Listenin üzerine "Audi" ve "Nissan" değerini ekleyin.

result = arabalar + ['Audi', 'Nissan']

# 10- Listenin son elemanın yazınız.

del arabalar[-1]
result = arabalar

# 11- Listenin son elemanın tersten yazdırınız.

result = arabalar[::-1]

# 12- Aşağıdaki verileri bir liste içinde saklayınız.

#     studentA: Yiğit Bilgi   2010, (70,60,70)
#     studentB: Sena Turan    1999, (80,80,70)
#     studentC: Ahmet Turan   1998, (80,70,90)

studentA = ['Yiğit','Bilgi', 2010, [70, 60, 70]]
studentB = ['Sena', 'Turan', 1999, [80, 80, 70]]
studentC = ['Ahmet', 'Turan', 199, [80, 70, 90]]

# 13- Lİste elemanlarını ekrana yazdırınız.

result = studentA[0]
result = studentA[1]
result = studentA[3][1]

# result = f"Yiğit Bilgi 9 yaşında ve not ortalaması 66"

result = f"{studentA[0]} {studentA[1]} {2019-studentA[2]} yaşında ve not ortalaması {(studentA[3][0] + studentA[3][1] + studentA[3][2])/3}"


print(result)
