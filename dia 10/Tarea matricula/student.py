class Student: 
    
    def __init__(self, name, carne): 
        self.name = name 
        self.carne = carne
            
    def addStudent(self, Name, Carne): 
        student = {}
        carne = 0
        student['name', Carne] = input('Ingrese un nombre: '+ carne)
        ob = Student(Name, Carne) 
        ls.append(ob)
        carne = carne += 1 
      
    def displayStudent(self, ob): 
            print("Name   : ", ob.name) 
            print("Carne : ", ob.carne) 
            print("\n")     
            
    def searchStudent(self, id): 
        for i in range(ls.__len__()): 
            if(ls[i].carne == id): 
                return i        
                                  
    def deleteStudent(self, id): 
        i = obj.search(id)   
        del ls[i] 
      
    def updateStudent(self, id, No): 
        i = obj.search(id) 
        idStd = No 
        ls[i].carne = idStd; 
        
ls =[] 
obj = Student('', 0) 
  