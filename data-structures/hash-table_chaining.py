# 해쉬 테이블 충돌 해결 알고리즘 1
# Chaining (Open Hashing 기법 : 해쉬 테이블 저장공간 외의 공간을 활용)
# : 충돌이 일어나면, 링크드 리스트 자료 구조를 사용하여 데이터를 추가로 뒤에 연결시켜 저장

import hashlib

hash_table = list([0 for i in range(8)])

def get_key(data):
  hash_object = hashlib.sha256()
  hash_object.update(data.encode())
  hex_dig = hash_object.hexdigest()
  return int(hex_dig, 16) # 16진수의 문자열을 10진수(정수)로 변환

def hash_function(key):
  return key % 8

def save_data(data, value):
  index_key = get_key(data)
  hash_address = hash_function(index_key)
  if hash_table[hash_address] != 0:
    for index in range(len(hash_table[hash_address])): # 링크드 리스트대신 리스트로 비슷한 효과 내기
      if hash_table[hash_address][index][0] == index_key: # 데이터 update
        hash_table[hash_address][index][1] == value
        return
    hash_table[hash_address].append([index_key, value])
  else :
    hash_table[hash_address] = [[index_key, value]]
  
def read_data(data):
  index_key = get_key(data)
  hash_address = hash_function(index_key)
  if hash_table[hash_address] != 0:
    for index in range(len(hash_table[hash_address])):
      if hash_table[hash_address][index][0] == index_key:
        return hash_table[hash_address][index][1]
    return None
  else:
    return None

save_data('Dd', '11111')
save_data('David', '22222')

print(hash_table)
print(read_data('Dd'))
print(read_data('David'))