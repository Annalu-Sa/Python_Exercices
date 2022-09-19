radius = float(input("Give me a ray: "))
def CircleArea(a):
    import math
    area = math.pi * a**a
    return area
print("The circle area is ", CircleArea(radius), ".")