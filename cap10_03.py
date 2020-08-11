import string as st

fhand = open(input('Digite o nome do arquivo: '))
dic = dict()
for line in fhand:
    line = line.strip()
    line = line.lower()
    line = line.translate(line.maketrans('','', st.punctuation))
    for i in range(len(line)):
        llt = line[i]
        if llt ==' ' or llt in st.digits: continue
        dic[llt] = dic.get(llt,0)+1

ordlist = list(dic.items())
neo = []
for i,j in ordlist:
    neo.append((j,i))
neo.sort(reverse=True)

tot = 0
for t,x in neo:
    tot += float(t)

for f,l in neo:
    p = (float(f)/tot)*100
    print(l,p,'%',f)
