#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = set(my_list)
    new_num = 0

    for i in uniq_list:
        new_num += i

    return (new_num)

