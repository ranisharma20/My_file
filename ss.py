def p_size():
    f=open("ss.txt",mode="r")
    str=f.read()
    size=len(str)
    print(size)
p_size()