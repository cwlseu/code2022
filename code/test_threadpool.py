"""
注意：这个是我们日常开发中常用的

因为新建线程系统需要分配资源、终止线程系统需要回收资源，所以如果可以重用线程，则可以减去新建/终止的开销以提升性能。
同时，使用线程池的语法比自己新建线程执行线程更加简洁。
Python为我们提供了ThreadPoolExecutor来实现线程池，此线程池默认子线程守护。它的适应场景为突发性大量请求或需要大
量线程完成任务，但实际任务处理时间较短。


其中max_workers为线程池中的线程个数，常用的遍历方法有map和submit+as_completed。
"""
from time import sleep

# python version >= 3.2
from concurrent.futures import as_completed, ThreadPoolExecutor

def fun(a:int):
    return a**2

# 根据业务场景的不同，若我们需要输出结果按遍历顺序返回，我们就用map方法，
with ThreadPoolExecutor(max_workers=5) as executor:
    ans = executor.map(fun, [i for i in range(5)])
    for res in ans:
        print(res)


print("-------------------------------------------")
# 若想谁先完成就返回谁，我们就用submit+as_complete方法。尤其适合纯IO类的，不关心返回结果与输入之间的顺序关系
with ThreadPoolExecutor(max_workers=5) as executor:
    list = [i for i in range(5)]
    ans = [executor.submit(fun, i) for i in list]
    for res in as_completed(ans):
        print(res.result())