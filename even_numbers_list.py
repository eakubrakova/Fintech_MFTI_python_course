"""The function, which returns odd number from the given list of numbers"""


def even_numbers(lst_of_numbers) -> list:

    even_lst = []
    for num in lst_of_numbers:
        if num % 2 == 0:
            even_lst.append(num)
    return even_lst


lst_of_numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]  # a list of numbers, which is set up freely
print(even_numbers(lst_of_numbers))
