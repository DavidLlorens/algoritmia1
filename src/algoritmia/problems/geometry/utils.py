#coding: latin1
from collections import namedtuple #[utils

Point2D = namedtuple("Point2D", "x y")

def left(a: "Point2D", b: "Point2D", c: "Point2D") -> "bool":
    return (a.y-b.y)*(c.x-b.x) - (a.x-b.x)*(c.y-b.y) > 0

def right(a: "Point2D", b: "Point2D", c: "Point2D") -> "bool":
    return (a.y-b.y)*(c.x-b.x) - (a.x-b.x)*(c.y-b.y) < 0 #]utils

def triangle_area(a: "Point2D", b: "Point2D", c: "Point2D") -> "bool": #[tri
    return abs((a.y-b.y)*(c.x-b.x) - (a.x-b.x)*(c.y-b.y)) / 2 #]tri
