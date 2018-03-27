import threading

import time


# 线程运行
class ThreadDemo(threading.Thread):
    def run(self):
        for i in range(5):
            print("thread name: {}, number: {} ".format(self.name, i))
            time.sleep(1)


# 三个线程
def main():
    threads = [ThreadDemo() for i in range(3)]
    print(threads)
    for t in threads:
        t.start()


if __name__ == '__main__':
    main()
