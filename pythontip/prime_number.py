# prime_number
# for i in range(2, 100):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#
#     else:
#         print(i)

# Factorial
result = []
x = input("input a number")
n = 1
for i in range(1, int(x)+1):
    n = n * i
    result.append(n)

print(f"{x}个数字阶乘的过程为{result}")
