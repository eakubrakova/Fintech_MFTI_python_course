def triangle(p1, p2, p3):
    # Функция для вычисления сторон треугольника
    # По умолчанию параметры функции берутся из объемлющей области видимости
    def sides(p1, p2, p3):
        # Распаковываем кортежи для удобства, “;” означает новую строку кода
        x1, y1 = p1; x2, y2 = p2; x3, y3 = p3
        # Вычисляем стороны по теореме Пифагора
        a = ((x2 - x1) ** 2 + (y2 - y1)** 2) ** 0.5
        b = ((x3 - x1) ** 2 + (y3 - y1)** 2) ** 0.5
        c = ((x3 - x2) ** 2 + (y3 - y2)** 2) ** 0.5
        return a, b, c

    # Функция для вычисления периметра треугольника
    def calculate_perimeter_triangle(a, b, c):
        # Периметр — сумма всех сторон треугольника
        perimeter = a + b + c
        return perimeter

    # Функция для вычисления площади треугольника
    def calculate_area_triangle(a, b, c):
        # Вычисляем полупериметр
        # Значение perimeter берётся из объемлющей области видимости
        p = perimeter / 2
        # Вычисляем площадь по формуле Герона
        area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        return area
    a, b, c = sides(p1, p2, p3)
    perimeter = calculate_perimeter_triangle(a, b, c)
    area = calculate_area_triangle(a, b, c)
    result = {'a': a, 'b': b, 'c': c, 'perimeter': perimeter, 'area': area}
    return result

def check_exist_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False