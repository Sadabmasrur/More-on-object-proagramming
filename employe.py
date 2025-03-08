class Employee():
    
    def __init__(self):
        print("Employee created")
        
    def __del__(self):
        print("DEstructer called")
        

def Create_obj():
    print("Making an obj")
    print()
    
    
    obj=Employee()
    print()
    
    print("Function end...")
    print()
    return obj 

print("Calling Create_obj() function")

objReturn=Create_obj()

print("Program End")
print()         
        