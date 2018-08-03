import time
import threading

def loop1(in1):
    # ctime得到当前时间
    print('Start loop 1 at:',time.ctime())
    #把参数打印出来
    print("我是参数",in1)
    time.sleep(4)
    print('End loop 1 at:',time.ctime())
def loop2(in1,in2):
    # ctime得到当前时间
    print('Start loop 2 at:',time.ctime())
    #把参数打印出来
    print("我是参数",in1,"和参数",in2)
    time.sleep(2)
    print('End loop 2 at:',time.ctime())

def main():
    print("Starting at:",time.ctime())
    # 生成threading.Thread实例
    t1 = threading.Thread(target=loop1,args=("老王",))
    t1.start()

    t2 = threading.Thread(target=loop2,args=("王五","王柳"))
    t2.start()

    print("All done at:",time.ctime())
if __name__ == "__main__":
    main()
    # 一定要有while语句
    # 因为启动多线程后本程序就作为主线程存在
    # 如果主线程执行完毕，则子线程可能也需要终止
    while True:
        time.sleep(10)