def count_smalls_1(lst):
    i = 0
    small_items = 0
    while i < len(lst):
        if lst[i] < 30:
            small_items += 1
        i += 1
        return small_items
    return small_items

def count_smalls_2(lst):
    i = 0
    small_items = 0
    while i < len(lst) and lst[i] < 30:
        small_items += 1
        i += 1
    return small_items

def count_smalls_3(lst):
    i = 0
    small_items = 0
    while i < len(lst):
        if lst[i] < 30:
            small_items += 1
        i += 1
    return small_items

def count_smalls_4(lst):
    i = 0
    small_items = 0
    while i < len(lst):
        if lst[i] < 30:
            small_items += 1
        else:
            return small_items
        i += 1
    return small_items

lst = [5,10,20,25,30,40]
print(count_smalls_1(lst))
print(count_smalls_2(lst))
print(count_smalls_3(lst))
print(count_smalls_4(lst))