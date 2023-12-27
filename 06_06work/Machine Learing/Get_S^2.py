data = [21, 25, 62, 43]


def S_2():
    Sum = 0
    for i in data:
        Sum = i + Sum
    average = Sum / len(data)

    up_num = 0
    for i in data:
        every_num = (i - average) ** 2
        up_num = every_num + up_num
    print(up_num)
    S_2 = up_num / len(data)

    print(S_2)


data2 = [-16.75, -12.75, 24.25, 5.25]

for num in data2:
    num_2 = num ** 2
    # print(num_2)

# S_2()

print(pow(156.8958, 0.5))
