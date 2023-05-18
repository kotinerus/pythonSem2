wolne = []
for j in range(1,4):
    for i in range(1,11):
        if i==10:
            wolne.append(str(j)+str(10))
        else:
            wolne.append(str(j)+str(0)+str(i))
print(wolne)