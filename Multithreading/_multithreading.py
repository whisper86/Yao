# 线程， 进程
# 进程（资源单位）， 线程（执行单位）， 进程至少要有一个线程

# 启动每一个程序默认都会有一个主线程
# def func():
#     for i in range(1000):
#         print("func", i)
#
#
# if __name__ == "__main__":
#     func()
#     for i in range(1000):
#         print("main", i)

# 以上为一个单线程程序


# 多线程

from threading import Thread  # 线程类


def func():
    for i in range(1000):
        print("func", i)


if __name__ == "__main__":
    t = Thread(target=func())  # 创建线程并给线程安排任务
    t.start()  # Start the thread 多线程状态为可以开始工作状态，具体的执行时间由CPU决定

    for i in range(1000):
        print("main", i)
