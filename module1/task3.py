text = """
Python is an interpreted high-level programming language for general-purpose programming. Created by Guido van Rossum and first released in 1991, Python has a design philosophy that emphasizes code readability, notably using significant whitespace. It provides constructs that enable clear programming on both small and large scales. In July 2018, the creator Guido Rossum stepped down as the leader in the language community after 30 years.
Python features a dynamic type system and automatic memory management. It supports multiple programming paradigms, including object-oriented, imperative, functional and procedural, and has a large and comprehensive standard library.
Python interpreters are available for many operating systems. CPython, the reference implementation of Python, is open source software and has a community-based development model, as do nearly all of Python's other implementations. Python and CPython are managed by the non-profit Python Software Foundation. Привет из Харькова!
"""
special_symbols = {" ", "-", ".", ",", "\n", "'"}
list_of_text = list(text)
filter_obj = filter(lambda symbol: symbol not in special_symbols, list_of_text)
list_without_special_symbols = list(filter_obj)
map_obj = map(lambda symbol: symbol.lower(), list_without_special_symbols)
lower_case_list = list(map_obj)
set_of_text = set(lower_case_list)
dictionary = {}
for s in set_of_text:
    dictionary[s] = lower_case_list.count(s)
max_elem = max(dictionary.items(), key=lambda d: d[1])
print(max_elem)
