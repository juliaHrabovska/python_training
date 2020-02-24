def file_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "Kb", "Mb", "Gb")
    i = 0
    step = 1024
    while size_bytes >= step or -size_bytes >= step:
        size_bytes /= step
        i += 1

    if i >= len(size_name):
        i = len(size_name) - 1

    return_value = float('{:.1f}'.format(size_bytes))
    return f"{return_value}{size_name[i]}"
