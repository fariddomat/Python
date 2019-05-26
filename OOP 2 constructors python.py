class Car:
    def __init__(self,Name):
         self._Name=Name
    def GetOwner(self):
        print("Owner is ",self._Name)




def oop2():
    mycar=Car("Farid Domat")
    mycar.GetOwner()
    mcar=Car("m h")
    mcar.GetOwner()


oop2()