import re


def user_put_verification(*args):
    pattern = r'[^\.0-9]+'
    code = 0
    for i in args:
        if i[0] == '.' or i[-1] == '.':
            return True
        for j in i:
            if j == '.':
                if code == 1:
                    return True
                code = 1
            else:
                code = 0
        res = re.findall(pattern, i)
        if res:
            return res
    else:
        return ''
