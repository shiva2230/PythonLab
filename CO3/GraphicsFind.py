from Graphics import rectangle
from Graphics import circle
from Graphics.graphics3d import cuboid,sphere
l=int(input("Enter the length"))
b=int(input("Enter the breadth"))
print("Area=",rectangle.rectangleArea(l,b))
print("Perimeter=",rectangle.rectanglePerimeter(l,b))
r=int(input("Enter the radius of circle"))
print("Circle Area=",circle.circleArea(r))
print("Circle Perimeter=",circle.circlePerimeter(r))
r=int(input("Enter the cuboid length"))
r=int(input("Enter the cuboid breadth"))
print("Cuboid Area=",cuboid.cuboidArea(l,b,r))
r=int(input("Enter the radius of sphere"))
print("Sphere Volume",sphere.sphereVolume(r))

