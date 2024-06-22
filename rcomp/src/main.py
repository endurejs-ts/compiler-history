from tools import *

with open("../dist/index.prm", "r") as f:
    data = f.read()
    rdata = split_special_chars(data)
    redata = convert_numbers_in_array(rdata)

    mut = [redata[0], redata[1], redata[2]]
    if is_sequence_in_order(mut, "mut"):
        name = redata[3]
        if is_string_in_list(["_"], name):
            ...
    
    else:
        print("error")