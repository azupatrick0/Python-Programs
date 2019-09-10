# This function sorts a list of a numbers, odd numbers first then even numbers
def sort_list(list_of_numbers):
    try:
        result = []
        for odd_number in sorted(list(list_of_numbers)):
            if odd_number % 2 == 1:
                result.append(odd_number)
        for even_number in sorted(list(list_of_numbers)):
            if even_number % 2 == 0:
                result.append(even_number)
        return result
    except TypeError:
        print('Input should be a list of numbers')