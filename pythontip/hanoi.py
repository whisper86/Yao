def hanoi(n):
    if n == 0:
        return 0
    else:
        return 2 * hanoi(n - 1) + 1


n = input("输入汉诺塔的层数")

print(f"移动{n}层汉诺塔需要{hanoi(int(n))}步")
