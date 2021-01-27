def Outer():
    def Inner():
        print("Hi")

    Inner()

Outer()


import math
print(math.sin(math.pi))
print(math.sin(math.radians(90)))
print(math.sin(math.radians(180)))
print(math.sin(math.radians(270)))

def temp_convert(degree,unit):
    '''(float, string) -> degree, unit
    return value in opposite unit (f -> c and vice versa)

    >>>temp_convert(32,f)
    0 c
    >>>temp_convert(100,c)
    212 f
    '''
    if unit==("f"):
        return (((degree-32) * (5/9), "c"))
    if unit==("c"):
        return (((degree+32)* (9/5), "f"))
