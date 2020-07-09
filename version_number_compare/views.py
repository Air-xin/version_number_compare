import json

from django.http import JsonResponse
from django.shortcuts import render

from tools.list_element_compare_size import list_element_compare_size
from tools.list_element_type_change import list_element_type_change
from tools.str_division import str_division
from tools.user_put_verification import user_put_verification


def get_index(request):
    return render(request, 'index.html')


def version_compare(request):
    json_obj = json.loads(request.body)
    num1 = json_obj.get('num1')
    num2 = json_obj.get('num2')
    print(num1, num2)

    # 校验输入
    verification_res = user_put_verification(num1, num2)
    print(verification_res)
    if verification_res:
        return JsonResponse({'code': 1000, 'error': '版本号必须是阿拉伯数字，按字符.分割,且版本字符串不以点开始或结束，并且其中不能有两个连续的点'})

    # 按 . 分割
    division_res = str_division(num1, num2)
    print(division_res)
    if len(division_res[0]) > 4 or len(division_res[1]) > 4:
        return JsonResponse({'code': 1001, 'error': '请输入最多4级版本号，按字符.分割'})

    # 列表每个元素类型转换
    version1 = list_element_type_change(division_res[0], division_res[1])[0]
    version2 = list_element_type_change(division_res[0], division_res[1])[1]
    print(version1, version2)

    # 比较本版号大小
    res = list_element_compare_size(version1, version2)
    print(res)

    return JsonResponse({'code': 200, 'msg': res})
