from threading import Thread


class MyThread(Thread):
    def run(self):   # 固定的  当线程被执行的时候，被执行的时候就是Run（）
        for i in range(1000):
            print("子线程", i)


if __name__ == "__main__":
    t = MyThread()
    # t.run()  # 方法调用了 -> 单线程
    t.start() # 开始线程
    for i in range(1000):
        print("主进程", i)
        