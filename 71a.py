n= int(input())
words = []
for i in range (0,n):
    soz = input()
    if len(soz) <= 10:
        words.append(soz)
    else:
        ortasi = len(soz) -2
        words.append(soz[0] + str(ortasi) + soz[-1])

for word in words:
    print(word)

