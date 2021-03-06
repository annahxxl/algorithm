# 내장함수와 리스트 변수를 활용해서 해쉬 테이블 구현해보기
# 해쉬 함수 : key % 8, 해쉬 키 생성 : hash(data)
hash_table = list([0 for i in range(8)])

def get_key(data):
  return hash(data)

def hash_function(key):
  return key % 8

def save_data(data, value):
  hash_address = hash_function(get_key(data))
  hash_table[hash_address] = value
  
def read_data(data):
  hash_address = hash_function(get_key(data))
  return hash_table[hash_address]

save_data('Andy', '01011111111')
save_data('Dave', '01022222222')

print(hash_table)
print(read_data('Dave'))