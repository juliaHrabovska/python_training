l = [1, [], 2, [-19, 700, 0, [90, 33, [18, 77, [0, ], -2], 11, 16], -100]]

max_value = l[0]
min_value = l[0]
sum_of_elem = 0
count_of_elem = 0


def iterate_list(list_of_elem):
    global max_value, min_value, sum_of_elem, count_of_elem
    for elem in list_of_elem:
        if isinstance(elem, list):
            if len(elem) != 0:
                iterate_list(elem)
            else:
                continue
        else:
            max_value = max(elem, max_value)
            min_value = min(elem, min_value)
            sum_of_elem += elem
            count_of_elem += 1


iterate_list(l)
print(f"Max value from the list is {max_value}")
print(f"Min value from the list is {min_value}")
print("Average value from the list is ", sum_of_elem / count_of_elem)
