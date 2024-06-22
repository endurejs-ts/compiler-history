import re

def convert_to_array(rbc):
    tokens = re.findall(r'\S+|\s', rbc)

    result = []
    for token in tokens:
        if token.isspace():
            result.append(token)
        else:
            if token.isdigit():
                result.append(int(token))
            else:
                result.append(token)
    
    return result

def split_special_chars(array):
    result = []
    for item in array:
        parts = re.findall(r'\w+|[^\w\s]', str(item))
        result.extend(parts)

    return result

def convert_numbers_in_array(array):
    result = []
    for item in array:
        if item.isdigit():
            result.append(int(item))
        else:
            result.append(item)

    return result

def is_sequence_in_order(lst, sequence):
    if len(lst) != len(sequence):
        return False
    
    for i in range(len(lst)):
        if lst[i] != sequence[i]:
            return False
    
    return True

def is_string_in_list(my_list, my_string):
    return any(element == my_string for element in my_list)