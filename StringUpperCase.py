class IOString:
    
    
    #constructor meathod
    def __init__(self):
        self.str=" "
        
        
    def GetString(self):
        self.str=input("Enter a string: ")   
        
    def printString(self):
        print(f"Result is: {self.str.upper()}")
        
        
string1=IOString()

#Calling a MEATHOD!!
string1.GetString()
string1.printString()        