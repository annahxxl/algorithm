# Max Heap 구현

class Heap:
    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(None) # 1번 index부터 시작
        self.heap_array.append(data)
      
    def move_up(self, inserted_idx): # 위치를 바꿔야 하는지 판별하는 메서드
        if inserted_idx <= 1:
            return False
        
        parent_idx = inserted_idx // 2
        if self.heap_array[inserted_idx] > self.heap_array[parent_idx]:
            return True
        else:
            return False
    
    def insert(self, data):
        if len(self.heap_array) == 0:
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True
        
        self.heap_array.append(data)
        
        inserted_idx = len(self.heap_array) - 1
        
        while self.move_up(inserted_idx):
            parent_idx = inserted_idx // 2
            self.heap_array[inserted_idx], self.heap_array[parent_idx] = self.heap_array[parent_idx], self.heap_array[inserted_idx] # swqp
            inserted_idx = parent_idx
        
        return True
      
heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)
print(heap.heap_array)