import time
from threading import Thread

class CountdownTask:
    def __init__(self):
        self.running = True

    def terminate(self):
        self._running = False

    def run(self,n):
        while self._running and n > 0:
            print('ˇ倒數計時：', n)
            n -= 1
            time.sleep(1)

c = CountdownTask()
t = Thread(target=c.run,args=(10,))
t.start()
time.sleep(5)
c.terminate()
t.join()
print('執行緒手動中斷')