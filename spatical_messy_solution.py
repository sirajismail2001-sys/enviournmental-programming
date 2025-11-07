#### exercise average

f = open("D:/enviournmental programming/P_June2019.asc", "r")
text= f.read()
print(text)
f=open("D:/enviournmental programming/P_June2019.asc", "r")
for line in f:
    print (line)
    lines = f.readlines()
data_lines = lines[6:]
data=[]
ncols= int(f.readlines().split()[1])
nrows= int(f.readlines().split()[1])
for i in range (3):
    f.readlines()
  ###what is this

NA = float (f.readlines().split()[1])

DATA = f.readlines()

data_splitted = []
for row in DATA:
    data_splitted.append(row.split())

DATA_float = []
for row in data_splitted:
    DATA_float.append([float(i)for i in row])

n = 0
total = 0
for i in range (nrows):
    for j in range(ncols):
        if DATA_float[i][j]!=NA:
            total = total+DATA_float[i][j]
            n = n+1
Average_P=total/n
print(Average_P)


x = 2+2

