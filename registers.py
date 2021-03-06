from register import Register
from tabulate import tabulate


class Registers(object):
    
    def __init__(self, size):
        self.registerList = []
        self.IntegisterList = []
        self.size = size
        register = Register("", 0)
        for i in range(size):
            self.registerList.append(register)
    
    def getRegister(self, number):
        return self.registerList[number]

    def editRegister(self, register, number):
        """
        Cambia el contenido de un registro por otro
        """
        self.registerList[number] = register

    def updateRegisterTag(self,tag, number):
        reg = Register(tag, self.registerList[number].valueI)
        self.editRegister(reg, number)

    def updateRegisterByTag(self, tag, register): 
        """
        Cambia el contenido de los registros que contengan el tag por otro
        """
        for i in range(self.size):
            if(self.registerList[i].Qi == tag):
                self.editRegister(register, i)


    def printRegisters(self):
        regs = self.iterateRegisters()
        print tabulate(regs, headers = ['Registro','Qi', 'valueI'], tablefmt='fancy_grid')

    def iterateRegisters(self):
        """
        Transforma los registros en un arreglo bidimensional, para poder utilizar la libreria tabulate.
        """
        arr = []
        for i in range(self.size):
            temp = []
            temp.append("F" + str(i))
            reg = self.registerList[i]
            temp.append(reg.Qi)
            temp.append(reg.valueI)
            arr.append(temp)
        return arr