my_file=open("file-question.txt","w")
list=["Kotak  " , "HDFC ", "RBL ","SBI ","Bank of Baroda"]
i=0
while i<len(list):
    print(list[i])
    i=i+1
my_file.close()