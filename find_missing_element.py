def missingelement(my_list):
    length = len(my_list)
    total = int(((length + 1) * (length + 2)) / 2)
    summation = sum(my_list)
    return total - summation


print(missingelement([1, 2, 3, 4, 6, 7]))
