# A Class for Taking Points 
class Point:
    
    """ 
        
        *Purpose of this Code : This is a function designed to find Euclidean Distance,
         Distance from Origin,Shortest Distance and Point on the Line.
        * Input : You have to input 4 coordinates like 1,2 and 3,4 in the form (1,2) and (3,4)
          and store them separately in a variable as given billow in the code.
          Finally, then you can use any of the function i.e Euclidean Distance(Enter Input Here).
        * Output : After providing inputs, this code will generate answers of your coordinates
          just like bellow.
         
         """
    # Constructor to initiate parameters and attributes
    def __init__(self,x,y):
        self.x_cod = x
        self.y_cod = y
    
    # A Magic Method to make a mathematics like form of the input and output    
    def __str__(self):
        return '<{},{}>'.format(self.x_cod,self.y_cod)
    
    # A function to find Euclidean Distance
    def Euclidean_distance(self,other):
        return ((self.x_cod - other.x_cod)**2 + (self.y_cod - other.y_cod)**2)**0.5  # Formula for Euclidean Distance
    
    # A function to find Distance from the Origin
    def distance_from_origin(self):
        return (self.x_cod**2 + self.y_cod**2)**0.5  # Formula for Distance from Origin. This is another way to find distance 
        #return self.Euclidean_distance(Point(0, 0))

# Another Class for taking Lines        
class Line:
    # Constructor to initiate attributes and parameters
    def __init__(self,A,B,C):
        self.A = A
        self.B = B
        self.C = C
    
    # A Magic Method to make a mathematics like form of the input and output    
    def __str__(self):
        return '{}x + {}y + {} = 0'.format(self.A,self.B,self.C)
    
    # A function to find Point on a Line
    def point_on_line(line,point):
        if line.A*point.x_cod + line.B*point.y_cod + line.C == 0:  # Formula for Point on a Line
            return "point lies on the line"

        else:
            return "point does not lies on the line"
     
    # A function to find Shortest Distance   
    def Shortest_distance(line,point):
        return abs(line.A*point.x_cod + line.B*point.y_cod +line.C) /(line.A**2 + line.B**2)**0.5  # Formula for Shortest Distance
    
    
### OBJECTS AREA ---------> PROVIDE INPUTS HERE JUST LIKE BELLOW
   
# p1 = Point(3, 5)
# # p2 = Point(10, 10)
# # print(p1.Euclidean_distance(p2))
# print(p1.distance_from_origin())
p1 = Line(1, 3, 5)
p2 = Point(3,9)
print(round(p1.Shortest_distance(p2)))


