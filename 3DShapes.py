from math import pi

#---------------------------------------CUBE------------------------------------
    
class Cube:
    
    def volume(args):
        #Checking if the Argument passed is an Iterable...
        #...and Returning an Iterable
        if type(args) is list or type(args) is tuple or type(args) is set:
            return [dimension*dimension*dimension for dimension in args]

        #Checking if the Argument passed is an Int or a Float...
        #...and Returning an Int or a Float
            
        elif type(args) is int or type(args) is float:
            dimension = args
            return dimension*dimension*dimension

    def curvedSurfaceArea(args):
        #if the Argument passed is an Iterable...
        #...then Returning an Iterable
        if type(args) is list or type(args) is tuple or type(args) is set:
            return [4*dimension*dimension for dimension in args]

        #if the Argument passed is an Int or a Float...
        #...then Returning an Int or a Float
            
        elif type(args) is int or type(args) is float:
            dimension = args
            return 4*dimension*dimension

    def totalSurfaceArea(args):
        #if the Argument passed is an Iterable...
        #...then Returning an Iterable
        if type(args) is list or type(args) is tuple or type(args) is set:
            return [6*dimension*dimension for dimension in args]

        #if the Argument passed is an Int or a Float...
        #...then Returning an Int or a Float
            
        elif type(args) is int or type(args) is float:
            dimension = args
            return 6*dimension*dimension

#----------------------------------CUBOID---------------------------------------

class Cuboid:

    def volume(*args):
        if len(args) == 1:
            list_dimension = [dimension for arg in args for dimension in arg]
            return [length*breadth*height for length,breadth,height in list_dimension]

        if len(args) == 3:                
            length, breadth, height = args[0], args[1], args[2]
            return length*breadth*height
        

    def curvedSurfaceArea(*args):
        if len(args) == 1:
            list_dim = [dimension for arg in args for dimension in arg]
            return ([2*height*(length+breadth)
                     for length,breadth,height in list_dim])

        if len(args) == 3:                
            length,breadth, height = args[0], args[1], args[2]
            return 2*height*(length+breadth)

    def totalSurfaceArea(*args):
        if len(args) == 1:
            list_dim = [dimension for arg in args for dimension in arg]
            return ([2*(length*breadth + breadth*height + height*length)
                     for length,breadth,height in list_dim])

        if len(args) == 3:                
            length,breadth, height = args[0], args[1], args[2]
            return 2*(length*breadth + breadth*height + height*length)

#------------------------------------SPHERES------------------------------------- 

class Sphere:
    
    def volume(args):
        #Checking if the Argument passed is an Iterable...
        #...and Returning an Iterable
        if type(args) is list or type(args) is tuple or type(args) is set:
            return [(4/3)*pi*radius*radius*radius for radius in args]

        #Checking if the Argument passed is an Int or a Float...
        #...and Returning an Int or a Float
            
        elif type(args) is int or type(args) is float:
            radius = args
            return (4/3)*pi*radius*radius*radius

    def curvedSurfaceArea(args):
        #if the Argument passed is an Iterable...
        #...then Returning an Iterable
        if type(args) is list or type(args) is tuple or type(args) is set:
            return [4*pi*radius*radius for radius in args]

        #if the Argument passed is an Int or a Float...
        #...then Returning an Int or a Float
            
        elif type(args) is int or type(args) is float:
            radius = args
            return 4*pi*radius*radius

class HemiSphere:
    
    def volume(args):
        #Checking if the Argument passed is an Iterable...
        #...and Returning an Iterable
        if type(args) is list or type(args) is tuple or type(args) is set:
            return [(2/3)*pi*radius*radius*radius for radius in args]

        #Checking if the Argument passed is an Int or a Float...
        #...and Returning an Int or a Float
            
        elif type(args) is int or type(args) is float:
            radius = args
            return (2/3)*pi*radius*radius*radius

    def curvedSurfaceArea(args):
        #if the Argument passed is an Iterable...
        #...then Returning an Iterable
        if type(args) is list or type(args) is tuple or type(args) is set:
            return [2*pi*radius*radius for radius in args]

        #if the Argument passed is an Int or a Float...
        #...then Returning an Int or a Float
            
        elif type(args) is int or type(args) is float:
            radius = args
            return 2*pi*radius*radius

    def totalSurfaceArea(args):
        #if the Argument passed is an Iterable...
        #...then Returning an Iterable
        if type(args) is list or type(args) is tuple or type(args) is set:
            return [3*pi*radius*radius for radius in args]

        #if the Argument passed is an Int or a Float...
        #...then Returning an Int or a Float
            
        elif type(args) is int or type(args) is float:
            radius = args
            return 3*pi*radius*radius

#------------------------------------CYLINDER------------------------------------- 

class Cylinder:

    def volume(*args):
        if len(args) == 1:
            list_dimension = [dimension for arg in args for dimension in arg]
            return [pi*radius*radius*height for radius,height in list_dimension]

        if len(args) == 2:                
            radius, height = args[0], args[1]
            return pi*radius*radius*height
        

    def curvedSurfaceArea(*args):
        if len(args) == 1:
            list_dim = [dimension for arg in args for dimension in arg]
            return [2*pi*radius*height for radius,height in list_dim]

        if len(args) == 2:                
            radius, height = args[0], args[1]
            return 2*pi*radius*height

    def totalSurfaceArea(*args):
        if len(args) == 1:
            list_dim = [dimension for arg in args for dimension in arg]
            return [2*pi*radius*(radius+height) for radius,height in list_dim]

        if len(args) == 2:                
            radius, height = args[0], args[1]
            return 2*pi*radius*(radius+height)

#-------------------------------------CONE-------------------------------------- 

class Cone:

    def volume(*args):
        if len(args) == 1:
            list_dimension = [dimension for arg in args for dimension in arg]
            return ([(1/3)*pi*radius*radius*height
                     for radius,height in list_dimension])

        if len(args) == 2:                
            radius, height = args[0], args[1]
            return (1/3)*pi*radius*radius*height

    def curvedSurfaceArea_withSlantHeight(*args):
        if len(args) == 1:
            list_dim = [dimension for arg in args for dimension in arg]
            return [pi*radius*length for radius,length in list_dim]

        if len(args) == 2:                
            radius, length = args[0], args[1]
            return pi*radius*length

    def curvedSurfaceArea_withHeight(*args):
        if len(args) == 1:
            list_dim = [dimension for arg in args for dimension in arg]
            return ([pi*radius*((radius**2 + height**2)**0.5)
                     for radius,height in list_dim])
        if len(args) == 2:                
            radius, height = args[0], args[1]
            return pi*radius*((radius**2 + height**2)**0.5)

    def totalSurfaceArea(*args):
        if len(args) == 1:
            list_dim = [dimension for arg in args for dimension in arg]
            return [pi*radius*(radius+length) for radius,length in list_dim]

        if len(args) == 2:                
            radius, length = args[0], args[1]
            return pi*radius*(radius+length)

    def slantHeight(*args):
        if len(args) == 1:
            list_dim = [dimension for arg in args for dimension in arg]
            return [(radius**2 + height**2)**0.5 for radius,height in list_dim]

        if len(args) == 2:                
            radius, height = args[0], args[1]
            return (radius**2 + height**2)**0.5
        
#------------------------------------FRUSTUM------------------------------------

class Frustum:

    def volume(*args):
        if len(args) == 1:
            list_dimension = [dimension for arg in args for dimension in arg]
            return ([(1/3)*pi*height*(r**2+R**2+r*R)
                     for r,R,height in list_dimension])

        if len(args) == 3:                
            r, R, height = args[0], args[1], args[2]
            return (1/3)*pi*height*(r**2+R**2+r*R)

    def curvedSurfaceArea_withSlantHeight(*args):
        if len(args) == 1:
            list_dim = [dimension for arg in args for dimension in arg]
            return [pi*length*(r+R) for r,R,length in list_dim]

        if len(args) == 3:                
            r, R, length = args[0], args[1], args[2]
            return pi*length*(r+R)

    def curvedSurfaceArea_withHeight(*args):
        if len(args) == 1:
            list_dim = [dimension for arg in args for dimension in arg]
            return ([pi*(r+R)*(height**2 + (R-r)**2)**0.5
                     for r,R,height in list_dim])
        if len(args) == 3:                
            r, R, height = args[0], args[1], args[2]
            return pi*(r+R)*(height**2 + (R-r)**2)**0.5

    def totalSurfaceArea(*args):
        if len(args) == 1:
            list_dim = [dimension for arg in args for dimension in arg]
            return [pi*length*(r+R)+pi*(r**2+R**2) for r,R,length in list_dim]

        if len(args) == 3:                
            r, R, length = args[0], args[1], args[2] 
            return pi*length*(r+R)+pi*(r**2+R**2)
        

    def slantHeight(*args):
        if len(args) == 1:
            list_dim = [dimension for arg in args for dimension in arg]
            return [(height**2 + (R-r)**2)**0.5 for r,R,height in list_dim]

        if len(args) == 3:                
            r, R, height = args[0], args[1], args[2]
            return (height**2 + (R-r)**2)**0.5
