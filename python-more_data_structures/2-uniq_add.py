#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_sum = 0
    unique_numbers = []

    for num in my_list:
        if num not in unique_numbers:
            unique_numbers.append(num)
            unique_sum += num

    return unique_sum

