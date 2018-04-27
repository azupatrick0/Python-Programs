def my_sort(list_of_number):
    list_of_number_one = list(list_of_number)
    sorted_list = sorted(list_of_number_one)
    list_of_number_two = []
    for i in sorted_list:
        if i %  2 == 1:
            list_of_number_two.append(i)
    for k in sorted_list:
        if k % 2 == 0:
              list_of_number_two.append(k)
    return list_of_number_two