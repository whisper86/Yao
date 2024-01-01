# from shlex import join
#
# number = input("input number")
#
# a = list(number)
#
# dict_number = {0: "零",
#                1: "壹",
#                2: "贰",
#                3: "叁",
#                4: "肆",
#                5: "伍",
#                6: "陆",
#                7: "柒",
#                8: "捌",
#                9: "玖"}
# character_list = []
# list1 = []
# for i in a:
#     i = int(i)
#     length = len(a)
#     if i in dict_number.keys():
#         a = dict_number.get(i)
#         character_list.append(a)
#     else:
#         pass
#     if length == 3:
#         print(len(character_list))
#     elif length == 2:
#         character_list.insert(2, "拾")
#     else:
#         continue
#
# print(str(character_list) + "圆")
char_number = ['零', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖']
char_unit = ['拾', '佰', '仟']


def convert(n):
    if n == 0:
        return ""
    if n < 10:
        return char_number[n]
    if len(str(n)) > 4:
        if (n % 10000) // 1000 == 0 and n % 10000 != 0:
            return convert(n // 10000) + "万零" + convert(n % 10000)
        return convert(n // 10000) + "万" + convert(n % 10000)
    tmp = 10 ** (len(str(n)) - 1)
    if len(str(n)) - len(str(n % tmp)) > 1 and n % 10 != 0:
        return convert(n // tmp) + char_unit[
        len(str(n)) - 2] + '零' + convert(n % tmp)
    return convert(n // tmp) + char_unit[len(str(n)) - 2] + convert(n % tmp)


if a == 0:
    print('零圆')
elif a < 0:
    print('负' + convert(abs(a)) + '圆')
else:
    print(convert(a) + '圆')
