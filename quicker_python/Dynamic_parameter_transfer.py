# 动态传参：给出多个位置参数，一次性接受
# * ：动态接受位置参数， 自动打包成元祖

# def Eat(*food):  # 可以接受任意个位置参数
#     print(food)
#
#
# Eat("rice")
# Eat("rice", "soup", "chicken")
# Eat("beef", "sheep")

# ** 动态接受关键字参数,接受到的参数是字典

# def Eat(** food):
#     print(food)
#
#
# Eat(main_food="noddles",slide_food="Stewed Beef with Potatoes")

# 实参
# 1 位置参数
# 2 关键字参数
# 3 混合参数，先位置，后关键字

# 形参
# 1 位置参数
# 2 默认值参数
# 3 动态传参
#   混合着使用，一定要注意， 代码的顺序
#    正确的顺序： 位置参数 *args放前 默认值参数 **kwargs

def func(a, *args, c="呵呵"):
    print(a, args, c)


# * args 收走了所有的位置参数
func("bye") # c使用了默认值，args没有数据
func("hello", "no_hello")
func("hello", "no_hello", "haha")
