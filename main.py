s, s1 = [], []
mat, rus, fiz = [], [], []

f = open('students.txt', 'r')
for line in f:
    s = line.strip().split(';')
    s = list(s[1:])
    for i in range(len(s)):
        s[i] = int(s[i])
    s1.append(s)
    mat.append(s[0])
    fiz.append(s[1])
    rus.append(s[2])

ouf = open('result.txt', 'w')
for i in range(len(s1)):
    ouf.write(str(sum(s1[i]) / len(s1[i])) + '\n')

ouf.write(str(sum(mat) / len(mat)) + ' ' + str(sum(fiz) / len(fiz)) + ' ' + str(sum(rus) / len(rus)))
