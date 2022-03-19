from time import sleep
import threading

def music(music_name):
    for i in range(2):
        print('正在听{}-{}'.format(music_name, i))
        sleep(1)
        print('music over-{}'.format(i))

def game(game_name):
    for i in range(2):
        print('正在玩{}-{}'.format(game_name, i))
        sleep(3)
        print('game over-{}'.format(i))

threads = []
t1 = threading.Thread(target=music,args=('稻香',))
threads.append(t1)
t2 = threading.Thread(target=game,args=('飞车',))
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        # t.setDaemon(True)
        t.start()

    for t in threads:
        t.join()
    print('主线程运行结束')