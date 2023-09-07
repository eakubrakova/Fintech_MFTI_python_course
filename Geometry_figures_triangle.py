def triangle(p1, p2, p3):
    def sides(p1, p2, p3):
        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3
        a = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        b = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5
        c = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
        return a, b, c

    def calculate_perimeter_triangle(a, b, c):
        perimeter = a + b + c
        return perimeter

    def calculate_area_triangle(a, b, c):
        p = perimeter / 2
        area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        return area

    a, b, c = sides(p1, p2, p3)
    perimeter = calculate_perimeter_triangle(a, b, c)

    def check_exist_triangle(a, b, c):
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Треугольник не существует")

    check_exist_triangle(a, b, c)

    area = calculate_area_triangle(a, b, c)
    result = {'a': a, 'b': b, 'c': c, 'perimeter': perimeter, 'area': area}

    return result













