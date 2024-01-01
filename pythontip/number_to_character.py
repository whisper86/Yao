# 参考代码，如嫌啰嗦，建议删除，一行搞定
# 需求
# 银行在打印票据的时候，常常需要将阿拉伯数字表示的人民币金额转换为大写表示，现在请你来完成这样一个程序。
# 在中文大写方式中，0到10以及100、1000、10000被依次表示为：    零 壹 贰 叁 肆 伍 陆 柒 捌 玖 拾 佰 仟 万
# 以下的例子示范了阿拉伯数字到人民币大写的转换规则：
# 1	壹圆
# 11	壹拾壹圆
# 111	壹佰壹拾壹圆
# 101	壹佰零壹圆
# -1000	负壹仟圆
# 1234567	壹佰贰拾叁万肆仟伍佰陆拾柒圆
# 现在给你一个整数a(|a|<100000000), 请你打印出人民币大写表示.
# 例如：a=1
# 则输出：壹圆
# 注意：请以Unicode的形式输出答案。提示：所有的中文字符，在代码中直接使用其Unicode的形式即可满足要求，中文的Unicode编码可以通过如下方式获得：u'壹'。
# 注意：代码无需声明编码！！不要在代码头部声明文件编码，否则会导致语法错误！

"""
 零 壹 贰 叁 肆 伍 陆 柒 捌 玖 拾 佰 仟 万
"""
dict_number = {0: "零",
               1: "壹",
               2: "贰",
               3: "叁",
               4: "肆",
               5: "伍",
               6: "陆",
               7: "柒",
               8: "捌",
               9: "玖"}

a = input("输入数字金额")


def solve_it(a):
    """
    pythontip oj不同于传统oj，代码里面直接使用变量，无需要提前声明，免去复杂的输入解析
    life is short, so i user python~
    you can use variables a
    """

    number_list = list(a)
    for i in number_list:
        x = int(i)
        for key in dict_number.keys():
            if x == dict_number.keys:
                character = dict_number.keys()
                return character  # your answer

            else:
                pass


print(solve_it(a))  # 答案需要输出
