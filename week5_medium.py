import math

class QuadraticEquation :
    def __init__(self, a , b, c) :
        self.a = a
        self.b = b
        self.c = c

    def discriminant(self) :
        self.disc = self.b**2 - (4 * self.a * self.c)
        return self.disc
    
    def solve(self) :
        if self.disc >= 0 :
            self.r = ((-self.b + math.sqrt(self.disc)) / (2 * self.a), (-self.b - math.sqrt(self.disc)) / (2 * self.a))
        else :
            self.r = ((-self.b / (2 * self.a)),(math.sqrt(-self.disc) / (2 * self.a))), ((-self.b / (2 * self.a)),(-math.sqrt(-self.disc) / (2 * self.a)))
        return self.r
        
class Point :
    def __init__(self, x, y) :
        self.x = x
        self.y = y
        
    def distance_to(self, other_point) :
        dist = math.sqrt(abs((self.x - other_point.x)**2) + ((self.y - other_point.y)**2))
        return round(dist, 2)
    
print("Select an Operation:")
print("1. Solve Quadratic Equation")
print("2. Calculate Distance Between Two Points")
answer = float(input("Your choice: "))

if answer == 1 :
    a, b, c = map(float, input("Enter coefficients a, b, and c for the quadratic equation (ax^2 + bx + c): ").split())
    Eq = QuadraticEquation(a, b, c)
    disc = Eq.discriminant() 
    roots = Eq.solve()
    print(f"The roots of the equation are: {roots}")

elif answer == 2 :
    x, y = map(float, input("Enter the cordinates of the first point (x, y): ").split())
    x2, y2 = map(float, input("Enter the cordinates of the second point (x, y): ").split())
    p = Point(x, y)
    other_point = Point(x2, y2)
    dist = p.distance_to(other_point)
    print(f"The distance between the points is: {dist}")

else :
    print("Invalid input!")


    
       
        
