import re
lst = ['piasdf-1', 'piasdasdc-3', 'pisdfgsc-2', '34pic-10', '3pic-6']
# lst.sort(key=lambda l: int(re.findall('-', l)[0]))  # 找出字符串中的数字并依据其整形进行排序
# print(lst)
# result = ['pic-1', 'pic-2', 'pic-3', 'pic-6', 'pic-10']  # 符合预期按顺序排序
print(sorted(lst, key=lambda info: (int(re.findall(r'-(\d+)', info)[0]))))