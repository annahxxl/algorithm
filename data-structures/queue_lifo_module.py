# Last-In, First-Out : 나중에 입력된 데이터가 먼저 출력되는 구조 (스택 구조라고 보면 됨)
import queue

data_queue = queue.LifoQueue()

data_queue.put('funcoding')
data_queue.put(1)

print('queue size : ', data_queue.qsize())
print(data_queue.get())
print(data_queue.get())