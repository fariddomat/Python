def exc():
    try:
        readFile=open("test.txt","r")
        for line in readFile:
            print(line)
        readFile.close()
    except IOError:
        print("File not found")
    else:
      print("File is readed")



exc()
