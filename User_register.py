# Функция для регистрации пользователей
def register(surname, name, date, middle_name=None, registry=None):
    # Вспомогательная функция для предобработки даты
    def preprocessing_date(date):
        # Разделяем строку по символу точки
        day, month, year = date.split('.')
        # Преобразуем все данные к типу данных int
        day, month, year = int(day), int(month), int(year)
        return day, month, year

    # Функция для проверки корректности даты
    def check_date(day, month, year):
        if not (isinstance(day, int) and isinstance(month, int) and isinstance(year, int)):
            return False

        if year < 1900 or year > 2022:
            return False

        if month < 1 or month > 12:
            return False

        if month in [4, 6, 9, 11] and (day < 1 or day > 30):
            return False

        if month == 2:
            if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                if day < 1 or day > 29:
                    return False
            else:
                if day < 1 or day > 28:
                    return False

        if day < 1 or day > 31:
            return False

        return True

    # Если список не был передан — создаём пустой список
    if registry is None:
        registry = list()

    # Разделяем дату на составляющие
    day, month, year = preprocessing_date(date)

    # Проверяем корректность даты
    if not check_date(day, month, year):
        raise ValueError("Invalid Date!")

    # Добавляем данные в список
    registry.append((surname, name, middle_name, day, month, year))

    return registry
