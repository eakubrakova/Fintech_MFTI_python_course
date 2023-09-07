## Введите свое решение ниже
def semi_axes(p1, p2, p3):
    a = ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5
    b = ((p3[0] - p1[0]) ** 2 + (p3[1] - p1[1]) ** 2) ** 0.5
    return a, b

def calculate_area_ellipse(a, b):
    area = pi * a * b
    return area

def calculate_length_ellipse(a, b):
    length = 2 * pi * ((a**2 + b**2)/2) ** 0.5
    return length

def ellipse(p1, p2, p3):
    a, b = semi_axes(p1, p2, p3)
    area = calculate_area_ellipse(a, b)
    length = calculate_length_ellipse(a, b)
    return {'a': round(a, 3),  'b': round(b,3), 'length': round(length, 3), 'area': round(area,3)}

pi = 3.1416
print(ellipse(p1=(3, 2.5), p2=(4.5, 2.5), p3=(3, 3.5)))

## {'a': 1.5, 'b': 1.0, 'length': 8.01, 'area': 4.712}

pi = 3.1416
print(ellipse(p1=(0, 0), p2=(0, 1), p3=(1, 0)))

## {'a': 1.0, 'b': 1.0, 'length': 6.283, 'area': 3.142}

pi = 3.14
print(ellipse(p1=(0, 0), p2=(0, 1), p3=(1, 0)))
## {'a': 1.0, 'b': 1.0, 'length': 6.28, 'area': 3.14}