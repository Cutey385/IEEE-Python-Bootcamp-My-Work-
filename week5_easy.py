def bosluk_birak(func) :
        def wrapper(*args, **kwargs) :
            print("\n")
            return func(*args, **kwargs)
        return wrapper
    
def buyut(func) :
    def wrapper(*args, **kwargs) :
        uppercase = func(*args, **kwargs).upper()
        return uppercase
    return wrapper

@bosluk_birak 
@buyut    
def birlestir(txt) :
   without_space = txt.replace(" ", "")
   return without_space

print("String: ")
print(birlestir("Hello World"))
     




