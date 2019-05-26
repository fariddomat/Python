def file1():
    out=open("test.txt","a")
    out.write(" \nfname:Farid")
    out.write(" \nlname:Domat")
    out.close()
    readFile=open("test.txt","r")
    for line in readFile:
        print(line)
    readFile.close()

file1()
