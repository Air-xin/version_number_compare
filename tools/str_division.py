def str_division(*args, character='.'):
    res_list = []

    for i in args:
        res = i.split(character)
        res_list.append(res)

    return res_list
