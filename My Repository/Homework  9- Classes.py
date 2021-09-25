# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
class Vehicle:
    def __init__(self,name,m,y,w):
        self.name = name
        self.model =m
        self.year = y
        self.weight = w
        
    def getName(self):
        return self.name

    def getModel(self):
        return self.model
        
    def getYear(self):
        return self.year
        
    def getWeight(self):
        return self.weight
    # Setters
    
    def setname(self,name):
        self.name = name
  
    def setModel(self,model):
        self.model = model
            
    def SetYear(self,year):
        self.year = year
            
    def SetWeight(self,weight):
        self.weight = weight
        
Vehicle1 = Vehicle("Tesla","Electric Car",2020,"3 Tonnes")

print(Vehicle1.getName())
        
