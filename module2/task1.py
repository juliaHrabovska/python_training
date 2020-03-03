def filter_list_by_for(list_of_elements):
    result_list = list()
    for elem in list_of_elements:
        if isinstance(elem, int):
            result_list.append(elem)
    return result_list


def filter_list_by_lambda(list_of_elements):
    return list(filter(lambda elem: isinstance(elem, int), list_of_elements))


def filter_list_by_list_comprehensions(list_of_elements):
    return [elem for elem in list_of_elements if isinstance(elem, int)]


l = [1, 2, '3', 4, None, 10, 33, 'Python', -37.5]
print(filter_list_by_for(l))
print(filter_list_by_lambda(l))
print(filter_list_by_list_comprehensions(l))