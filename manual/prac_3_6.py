radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))
volume = 3.14 * radius ** 2 * height
surface_area = 2 * 3.14 * radius * (radius + height)
print(f"Volume: {volume:.2f}, Surface Area: {surface_area:.2f}")