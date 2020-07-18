class Teacher: 
    
    def __init__(self, name, carneT): 
        self.name = name 
        self.carneT = carneT
            
    def addT(self, Name, carneT):
        Teacher = {}
        carneT = 0
        teacher['name', Carnet] = input('Ingrese un nombre: '+ carnet)
        ob = Teacher(Name, Carnet) 
        ls.append(ob)
        carnet ++ 
      
    def displayT(self, ob): 
            print("Name   : ", ob.name) 
            print("Carne : ", ob.carneT) 
            print("\n")     
            
    def searchT(self, id): 
        for i in range(ls.__len__()): 
            if(ls[i].carneT == id): 
                return i        
                                  
    def deleteT(self, id): 
        i = obj.search(id)   
        del ls[i] 
      
    def updateT(self, id, No): 
        i = obj.search(id) 
        idStd = No 
        ls[i].carneT = idStd; 
        
ls =['Eduardo', 1] 
obj = Teacher('', 0) 