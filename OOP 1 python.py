class Car:
    def GetOwner(self):
        print("Owner is ",self._Name)
    def SetOwner(self,Name):
        self._Name=Name



def OOP1():
    mycar=Car()
    mycar.SetOwner("Farid Domat")
    mycar.GetOwner()
    mcar=Car()
    mcar.SetOwner("m h")
    mcar.GetOwner()



OOP1()