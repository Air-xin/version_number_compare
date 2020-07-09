def list_element_compare_size(list1, list2):
    zip_list = zip(list1, list2)

    for i in zip_list:
        if i[0] > i[1]:
            return 1
        elif i[0] < i[1]:
            return -1
        else:
            continue

    else:
        if len(list1) > len(list2):
            for i in range(len(list2), len(list1)):
                if list1[i] > 0:
                    return 1
                else:
                    continue
            else:
                return 0

        elif len(list1) < len(list2):
            for i in range(len(list1), len(list2)):
                if list2[i] > 0:
                    return -1
                else:
                    continue
            else:
                return 0
        else:
            return 0
