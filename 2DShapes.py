from math import pi

#---------------------------------QUADRILATERALS----------------------------------    
class Square:
    
    def area(args):
        #Checking if the Argument passed is an Iterable...
        #...and Returning an Iterable
        if type(args) is list or type(args) is tuple or type(args) is set:
            return [dimension*dimension for dimension in args]

        #Checking if the Argument passed is an Int or a Float...
        #...and Returning an Int or a Float
            
        elif type(args) is int or type(args) is float:
            dimension = args
            return dimension*dimension
    
    def perimeter(args):
        #if the Argument passed is an Iterable...
        #...then Returning an Iterable
        if type(args) is list or type(args) is tuple or type(args) is set:
            return [4*dimension for dimension in args]

        #if the Argument passed is an Int or a Float...
        #...then Returning an Int or a Float
            
        elif type(args) is int or type(args) is float:
            dimension = args
            return 4*dimension
        
class Rectangle:
    
    def area(*args):
        if len(args) == 1:
            list_dimension = [dimension for arg in args for dimension in arg]
            return [length*breadth for length,breadth in list_dimension]

        if len(args) == 2:                
            length, breadth = args[0], args[1]
            return length*breadth
        

    def perimeter(*args):
        if len(args) == 1:
            list_dim = [dimension for arg in args for dimension in arg]
            return [2*(length+breadth) for length,breadth in list_dim]

        if len(args) == 2:                
            length,breadth = args[0], args[1]
            return 2*(length+breadth)

class Rhombus:
    
    def area(*args):
        if len(args) == 1:
            list_dimension = [diagonal for arg in args for diagonal in arg]
            return [0.5*diagonal_1*diagonal_2 for diagonal_1,diagonal_2 in list_dimension]

        if len(args) == 2:                
            diagonal_1,diagonal_2 = args[0], args[1]
            return 0.5*diagonal_1*diagonal_2

    def perimeter(args):
        if type(args) is list or type(args) is tuple or type(args) is set:
            return [4*dimension for dimension in args]
            
        elif type(args) is int or type(args) is float:
            dimension = args
            return 4*dimension
    

class Parallelogram:

    def area(*args):
        if len(args) == 1:
            list_dimension = [dimension for arg in args for dimension in arg]
            return [base*height for base,height in list_dimension]

        if len(args) == 2:                
            base, height = args[0], args[1]
            return base*height
        
    def perimeter(*args):
        if len(args) == 1:
            list_dim = [dimension for arg in args for dimension in arg]
            return [2*(length+breadth) for length,breadth in list_dim]

        if len(args) == 2:                
            length, breadth = args[0], args[1]
            return 2*(length+breadth)

class Trapezium:

    def area(*args):
        if len(args) == 1:
            list_dimension = [dimension for arg in args for dimension in arg]
            return [0.5*height*(a+c) for a,c,height in list_dimension]

        if len(args) == 3:                
            a, c, height = args[0], args[1], args[2]
            return 0.5*height*(a+c)

    def perimeter(*args):
        if len(args) == 1:
            list_dim = [dimension for arg in args for dimension in arg]
            return [a+b+c+d for a,b,c,d in list_dim]

        if len(args) == 4:                
            a, b, c, d = args[0], args[1], args[2], args[3]
            return (a+b+c+d)

#------------------------------------CIRCLES------------------------------------ 

class Circle:
    def area(args):

        if type(args) is list or type(args) is tuple or type(args) is set:
            return [pi*radius*radius for radius in args]

        #Checking if the Argument passed is an Int or a Float...
        #...and Returning an Int or a Float
            
        elif type(args) is int or type(args) is float:
            radius = args
            return pi*radius*radius

    def perimeter(args):
        #if the Argument passed is an Iterable...
        #...then Returning an Iterable
        if type(args) is list or type(args) is tuple or type(args) is set:
            return [2*pi*radius for radius in args]

        #if the Argument passed is an Int or a Float...
        #...then Returning an Int or a Float
            
        elif type(args) is int or type(args) is float:
            radius = args
            return 2*pi*radius

class SemiCircle:
    def area(args):

        if type(args) is list or type(args) is tuple or type(args) is set:
            return [0.5*pi*radius*radius for radius in args]

        #Checking if the Argument passed is an Int or a Float...
        #...and Returning an Int or a Float
            
        elif type(args) is int or type(args) is float:
            radius = args
            return 0.5*pi*radius*radius

    def perimeter(args):
        #if the Argument passed is an Iterable...
        #...then Returning an Iterable
        if type(args) is list or type(args) is tuple or type(args) is set:
            return [pi*radius for radius in args]

        #if the Argument passed is an Int or a Float...
        #...then Returning an Int or a Float
            
        elif type(args) is int or type(args) is float:
            radius = args
            return pi*radius

#---------------------------------TRIANGLES---------------------------------- 

class ScaleneTriangle:

    def area(*args):
        if len(args) == 1:
            list_dimension = [dimension for arg in args for dimension in arg]
            return ([(((a+b+c)/2)*(((a+b+c)/2)-a)*(((a+b+c)/2)-b)*(((a+b+c)/2)-c))**0.5
                     for a,b,c in list_dimension])
            #return [(s*(s-a)*(s-b)*(s-c))**0.5 for a,b,c in list_dimension]
        if len(args) == 3:                
            a, b, c = args[0], args[1], args[2]
            return (((a+b+c)/2)*(((a+b+c)/2)-a)*(((a+b+c)/2)-b)*
                    (((a+b+c)/2)-c))**0.5

    def perimeter(*args):
        if len(args) == 1:
            list_dim = [dimension for arg in args for dimension in arg]
            return [a+b+c for a,b,c in list_dim]

        if len(args) == 3:                
            a, b, c = args[0], args[1], args[2]
            return (a+b+c)

class IsoscelesTriangle:
    def area(*args):
        if len(args) == 1:
            list_dimension = [dimension for arg in args for dimension in arg]
            return [0.5*base*height for base,height in list_dimension]

        if len(args) == 2:                
            base, height = args[0], args[1]
            return 0.5*base*height

    def perimeter(*args):
        if len(args) == 1:
            list_dim = [dimension for arg in args for dimension in arg]
            return [(2*a)+base for a,base in list_dim] #a = One of parallel sides

        if len(args) == 2:                
            a, base = args[0], args[1]
            return (2*a)+base

class EquilateralTriangle:
    def area(args):
        #Checking if the Argument passed is an Iterable...
        #...if Yes, Returning also an Iterable
        if type(args) is list or type(args) is tuple or type(args) is set:
            return [((3/4)**0.5)*(dimension**2) for dimension in args]

        #Checking if the Argument passed is an Int or a Float...
        #...if Yes, Returning also an Int or a Float
            
        elif type(args) is int or type(args) is float:
            dimension = args
            return ((3/4)**0.5)*(dimension**2)

    def perimeter(args):
        #if the Argument passed is an Iterable...
        #...then Returning an Iterable
        if type(args) is list or type(args) is tuple or type(args) is set:
            return [3*dimension for dimension in args]

        #if the Argument passed is an Int or a Float...
        #...then Returning an Int or a Float
            
        elif type(args) is int or type(args) is float:
            dimension = args
            return 3*dimension

class RightAngleTriangle:
    def area(*args):
        if len(args) == 1:
            list_dimension = [dimension for arg in args for dimension in arg]
            return [0.5*base*height for base,height in list_dimension]

        if len(args) == 2:                
            base, height = args[0], args[1]
            return 0.5*base*height

    def perimeter(*args):
        if len(args) == 1:
            list_dim = [dimension for arg in args for dimension in arg]
            return [a+b+c for a,b,c in list_dim]

        if len(args) == 3:                
            a, b, c = args[0], args[1], args[2]
            return (a+b+c)
