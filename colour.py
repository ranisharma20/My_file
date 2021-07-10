my_file=open("colour.txt","w")
list= ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
i=0
while i<len(list):
    print(list[i])
    i=i+1
my_file.close()

