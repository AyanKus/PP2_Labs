def sphere_volume(radius):
    pi = 3.14159  
    volume = (4/3) * pi * (radius ** 3)
    return volume

radius = float(input("Enter the radius of the sphere: "))
print("Volume of the sphere with radius", radius, "is:", sphere_volume(radius))
