# module 사용 시 module명과 파일명이 달라야함
# -> 사용하려는 module과 동일한 이름의 파일이 존재하면 import 시 동일한 경로에 있는 파일을 먼저 인식하게 됨

# First-In, First-Out : 가장 일반적인 큐 자료 구조
import queue

data_queue = queue.Queue()

data_queue.put("funcoding")
data_queue.put(1)

print('queue size : ', data_queue.qsize())
print(data_queue.get())
print(data_queue.get())