def circle(p1, p2):
    def radius(p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        radius = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        return radius

    def calculate_circumference(radius):
        circumference = 2 * pi * radius
        return circumference

    def calculate_area_circle(radius):
        area = pi * radius ** 2
        return area

    radius_value = radius(p1, p2)
    circumference_value = calculate_circumference(radius_value)
    area_value = calculate_area_circle(radius_value)

    return {'radius': round(radius_value, 3), 'circumference': round(circumference_value,3), 'area': round(area_value, 3)}

pi = 3.1416
print(circle(p1=(3, 2.5), p2=(4, 4.5)))
## {'radius': 2.236, 'circumference': 14.05, 'area': 15.708}

pi = 3.1416
print(circle(p1=(0, 0), p2=(1, 1)))
## {'radius': 1.414, 'circumference': 8.886, 'area': 6.283}

pi = 3.14
print(circle(p1=(3, 2.5), p2=(4, 4.5)))
## {'radius': 2.236, 'circumference': 14.043, 'area': 15.7}