import threading

class Account:
    def __init__(self, card_id, balance):
        # 封装账户ID、账户余额的两个变量
        self.card_id= card_id
        self.balance = balance

def withdraw(account, money):
    # 进行加锁
    lock.acquire()
    # 账户余额大于取钱数目
    if account.balance >= money:
        # 吐出钞票
        print(threading.current_thread().name + "取钱成功！吐出钞票:" + str(money),end=' ')
        # 修改余额
        account.balance -= money
        print("\t余额为: " + str(account.balance))
    else:
        print(threading.current_thread().name + "取钱失败！余额不足")
    # 进行解锁
    lock.release()

def main():
    # 创建一个账户，银行卡id为8888，存款1000元
    acct = Account("8888" , 2000)

    # 模拟两个对同一个账户取钱
    # 在主线程中创建一把锁
    lock = threading.Lock()
    threading.Thread(name='窗口A', target=withdraw , args=(acct , 800)).start()
    threading.Thread(name='窗口B', target=withdraw , args=(acct , 800)).start()
    threading.Thread(name='窗口C', target=withdraw , args=(acct , 800)).start()


"""
如果我们的锁是`threading.Lock()`会发现这个程序只会打印“第一道锁”，而且程序既没有终止，也没有继续运行。
这是因为Lock锁在同一线程内第一次加锁之后还没有释放时，就进行了第二次acquire请求，导致无法执行release，
所以锁永远无法释放，这就是死锁。如果我们使用RLock就能正常运行，不会发生死锁的状态。
"""

def main2():
    """This class implements reentrant lock objects.

    A reentrant lock must be released by the thread that acquired it. Once a
    thread has acquired a reentrant lock, the same thread may acquire it
    again without blocking; the thread must release it once for each time it
    has acquired it.

    Lock被称为原始锁，一个线程只能请求一次；RLock被称为重入锁，可以被一个线程请求多次，即锁中可以嵌套锁

    当Lock处于锁定状态时，不属于特定线程，可在另一个线程中进行解锁释放；
    而RLock只有当前线程才能释放本线程上的锁，不可由其他线程进行释放，所以在使用RLock时，acquire与release必须成对出现，即解铃还须系铃人
    """
    lock.acquire()
    print('第一道锁')
    lock.acquire()
    print('第二道锁')
    lock.release()
    lock.release()

if __name__ == '__main__':
    lock = threading.Lock()
    main2()