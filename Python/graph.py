"This module contains some basic functions of coordinate geometry"

from math import sqrt
from typing import List, Tuple

__all__ = ["grad", "dist", "midpoint", "coordinates_equation", "grad_equation", "get_coordinates", "area", "get_shape", "perp_dist"]

Equation = str
Coordinate = Tuple[float or int, float or int]


def grad(coordinate1: Coordinate, coordinate2: Coordinate) -> float or int:

    "Returns the gradient or the slope of the line formed by the given coordinates"

    if coordinate1[0] == coordinate2[0]:
        return None
    
    else:
        return coordinate2[1] - coordinate1[1] / coordinate2[0] - coordinate1[0]
        
def dist(coordinate1: Coordinate, coordinate2: Coordinate) -> float or int:
    
    "Returns the distance between the two given coordinates"

    return str(pow(pow((coordinate2[0] - coordinate1[0]) , 2) + pow((coordinate2[1] - coordinate1[1]) , 2), (1 / 2)))


def midpoint(coordinate1: Coordinate, coordinate2: Coordinate) -> Coordinate:

    "Returns the midpoint coordinates of the line formed by given two coordinates"
    
    x = (coordinate2[0] + coordinate1[0]) / 2
    y = (coordinate2[1] + coordinate1[1]) / 2

    return f"({x}, {y})"

def isparallel(line1: List[Coordinate] or Tuple[Coordinate], line2: List[Coordinate] or Tuple[Coordinate]) -> bool:

    """Returns True if both lines are parallel to each other.
    If not so, it returns False"""

    if line1[0][0] == line1[1][0] and line2[0][0] == line2[1][0]:
        return True

    elif (line1[1][1] - (line1[0][1])) / (line1[1][0] - (line1[0][0])) == (line2[1][1] - (line2[0][1])) / (line2[1][0] - (line2[0][0])):
        return True

    return False

def isperpendicular(line1: List[Coordinate] or Tuple[Coordinate], line2: List[Coordinate] or Tuple[Coordinate]) -> bool:

    """Returns True if both lines are perpendicular to each other.
    If not so, it returns False"""

    if (line1[0][0] == line1[1][0] or line2[0][0] == line2[1][0]) and (line1[0][1] == line1[1][1] or line2[0][1] == line2[1][1]):
        return True

    elif (line1[1][1] - line1[0][1]) / (line1[1][0] - line1[0][0]) * (line2[1][1] - line2[0][1]) / (line2[1][0] - line2[0][0]) == -1:
        return True

    return False

def coordinates_equation(coordinate1: Coordinate, coordinate2: Coordinate) -> Equation:

    "Returns the equation of line formed by the two given coordinates in the form of 'y = mx + c'"
         
    if coordinate1[0] == coordinate2[0]:
        return f"x = {coordinate1[0]}"
    
    m = coordinate2[1] - coordinate1[1] / coordinate2[0] - coordinate1[0]
    c = coordinate1[1] - (m * coordinate1[0])

    if (coordinate2[1] - coordinate1[1]) == 0:
        return f"y = {coordinate1[1]}"
    
    elif c > 0:
        return f"y = {m}x + {c}"
    
    elif c < 0:
        return f"y = {m}x - {-(c)}"
    
    elif c == 0:
        return f"y = {m}x"

def grad_equation(coordinate: Coordinate, m: float or int) -> Equation:

    "Returns the equation of the line formed by the m (gradient) and the coordinate in the form of 'y = mx + c'"

    c = m * (-(coordinate[0])) + coordinate[1]

    if m == 0:
        return f"y = {coordinate[1]}"
    
    elif c > 0:
        return f"y = {m}x + {c}"
    
    elif c < 0:
        return f"y = {m}x - {-(c)}"
    
    elif c == 0:
        return f"y = {m}x"


def get_coordinates(m: float or int, c: float or int, x_range: Tuple[int, int]) -> List[Coordinate]: 
        
    """Takes m (gradient), c (y-intercept) and a tuple of range of values of 'x' to produce the value of y-coordinate for every value of x
    The equation should be in the form of 'y = mx + c' of which m and c should be the inputs"""
    
    cord_list = []

    for x in range(x_range[0], x_range[1] + 1):

        y = m * x + c
        cord_list.append((x, y))

    return cord_list
        

def area(lst: List[Coordinate]) -> float or int:
    
    """Takes in a list of coordinates to find the area of the polygon using shoelace formula.
The coordinates should be listed clockwise or counter-clockwise otherwise the result may come incorrect.
It takes minimum 3 coordinates because less than 3 coordinates can not make a shape"""

    lst.append(lst[0])

    if len(lst) - 1 > 2:
        
        lst_indx, lst_indx_2, answer1, answer2, final_answer = 0, 0, 0, 0, 0
        
        for _ in lst:
            calculation = lst [lst_indx][0] * lst [lst_indx + 1][1]
            answer1 += calculation
            lst_indx += 1
            if lst_indx == len(lst) - 1:
                break

        for _ in lst:
            calculation2 = lst [lst_indx_2][1] * lst [lst_indx_2 + 1][0]
            answer2 += calculation2
            lst_indx_2 += 1
            if lst_indx_2 == len(lst) - 1:
                break
        
        final_answer = 0.5 * abs(answer1 - answer2)

    else:
        raise TypeError(f"area expected minimum 3 arguments, {len(lst) - 1} were given.")

    if type(final_answer) == float:
        final_answer = str(final_answer)
        if final_answer.endswith(".0"):
            final_answer = final_answer[:-2]
            return int(final_answer)

    return final_answer

def get_shape(lst: List[Coordinate]) -> str:  

    """Returns the shape made when the given coordinates are connected together.
    The coordinates should be listed clockwise or counter-clockwise otherwise the result may come incorrect."""

    while len(lst) > 2:

        shape = "irregular polygon"
        
        if len(lst) == 3:
            shape =  "triangle"
        
        elif len(lst) == 4:
            if dist(lst[0], lst[1]) == dist(lst[1], lst[2]) == dist(lst[2], lst[3]) == dist(lst[3], lst[0]):
                if isparallel([lst[0], lst[1]], [lst[2], lst[3]]) and isparallel([lst[0], lst[3]], [lst[1], lst[2]]):
                    if isperpendicular([lst[0], lst[1]], [lst[1], lst[2]]) and isperpendicular([lst[1], lst[2]], [lst[2], lst[3]]):
                        shape = "square"

                    elif not isperpendicular([lst[0], lst[1]], [lst[1], lst[2]]) and not isperpendicular([lst[1], lst[2]], [lst[2], lst[3]]):
                        shape = "rhombus"         # needs to be checked
            
            elif dist(lst[0], lst[1]) == dist(lst[2], lst[3]) and dist(lst[3], lst[0]) == dist(lst[1], lst[2]):
                if isparallel([lst[0], lst[1]], [lst[2], lst[3]]) and isparallel([lst[0], lst[3]], [lst[1], lst[2]]):
                    shape = "rectangle"

                elif not isperpendicular([lst[0], lst[1]], [lst[1], lst[2]]) and not isperpendicular([lst[1], lst[2]], [lst[2], lst[3]]):
                        shape = "parallelogram"   # needs to be checked

            elif isparallel([lst[0], lst[1]], [lst[2], lst[3]]) or isparallel([lst[1], lst[2]], [lst[3], lst[0]]):
                if not isperpendicular([lst[0], lst[1]], [lst[1], lst[2]]) and not isperpendicular([lst[1], lst[2]], [lst[2], lst[3]]):
                    if not isperpendicular([lst[2], lst[3]], [lst[3], lst[0]]) and not isperpendicular([lst[3], lst[0]], [lst[0], lst[1]]):
                        shape = "trapezium"       # needs to be checked

        else:
            shape = "irregular polygon"

        break
    
    else:
        raise TypeError(f"get_shape expected minimum 3 arguments, {len(lst)} were given.")

    if len(lst) >= 5:
        return None
    
    return shape

def perp_dist(eq: List[int], point: List[int]) -> float:
    
    "Returns the perpendicular or the shortest distance between a point and a line or between two lines"
    
    assert len(eq) == 3, "eq expected values of a, b and c of the equation in the form of 'ax + by + c = 0'"
    assert len(point) == 2 or len(point) == 3, "point expected either the coordinates of x and y or values of a, b and c of equation"
    
    if len(point) == 2:
        return abs(((eq[0] * point[0]) + (eq[1] * point[1]) + eq[2]) / (sqrt(pow(eq[0], 2) + pow(eq[1], 2))))
    
    return abs((point[2] - eq[2]) / (sqrt(pow(eq[0], 2) + pow(eq[1], 2))))

#print(dist((4, 5), (3, -2)))
#print(grad((4, 10), (4, 5)))
#print(midpoint((4, 5), (3, -2)))
#print(coordinates_equation((4, 5), (3, -2)))
#print(grad_equation((-1, 8), -2))
#print(get_coordinates(-1.5, -2, (-4, 4)))
#print(area([(-1, 4), (0, -3), (5, 2)]))
#print(get_shape([(2, 5), (2, 2), (6, 2), (6, 5)]))
#print(isparallel([(0, 4), (5, 10)], [(0, 4), (5, 10)]))
#print(isperpendicular([(3, -4), (6, -1)], [(6, -3), (7, -5)]))
print(perp_dist([3, -4, 2], [4, 1]))