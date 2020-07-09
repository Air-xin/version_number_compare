def list_element_type_change(list1, list2):
    new_list1 = []
    new_list2 = []

    for i in list1:
        new_list1.append(int(i))

    for i in list2:
        new_list2.append(int(i))

    return (new_list1, new_list2)
