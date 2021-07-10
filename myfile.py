f=open("myfile.txt","r")
a=f.readlines()
i=0
while i<len(a):
    i=i+1
print(i)
f.close()
