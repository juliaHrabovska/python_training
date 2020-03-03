import fnmatch
import os


def find_files_by_pattern_in_folder(folder_path, pattern):
    elements_in_folder = list(os.walk(folder_path))
    if len(elements_in_folder) == 0:
        return list()
    result_list = list()
    for elem in elements_in_folder:
        root_path = elem[0]
        if len(elem[2]) != 0:
            for file_name in elem[2]:
                if fnmatch.fnmatch(file_name, pattern):
                    result_list.append(os.path.join(root_path, file_name))

    return result_list


print(find_files_by_pattern_in_folder("D:\PythonProjects\python_training\module2", "*.py"))
