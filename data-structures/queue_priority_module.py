# 데이터마다 우선순위를 넣어 우선순위가 높은 순으로 데이터 출력
import queue

data_queue = queue.PriorityQueue()

data_queue.put((10, 'korea')) # 튜플(우선순위 : 크기가 낮을수록 높음, 데이터)로 데이터 넣기
data_queue.put((5, 1))
data_queue.put((15, 'china'))

print('queue size : ', data_queue.qsize())
print(data_queue.get())
print(data_queue.get())
print(data_queue.get())