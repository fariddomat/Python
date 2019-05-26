


def Dic():
    Student=dict(Name="Farid",Age=23,Slary=850.5)
    Student['Name']="Farid Domat"
    Student["Dept"]="software engineer"
    print(Student,type(Student))
    del Student["Dept"]
    print(Student,type(Student))
    print(Student['Name'])
    print(Student['Age'])
    Student.clear()
    #print(Student,type(Student))
    
Dic()
