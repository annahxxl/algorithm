# 해쉬 테이블 충돌 해결 알고리즘 2
# Linear Probing (Close Hashing 기법 : 해쉬 테이블 저장공간 안의 공간을 활용)
# : 충돌이 일어나면, 해당 해쉬 주소의 다음 주소부터 맨 처음 나오는 빈 공간에 저장하는 기법 (저장 공간 활용도를 높이기 위한 기법)

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
    for index in range(hash_address, len(hash_table)):
      if hash_table[index] == 0:
        hash_table[index] = [index_key, value]
        return
      elif hash_table[index][0] == index_key: # 데이터 update
        hash_table[index][1] = value
        return
  else:
    hash_table[hash_address] = [index_key, value]
  
def read_data(data):
  index_key = get_key(data)
  hash_address = hash_function(index_key)
  if hash_table[hash_address] != 0:
    for index in range(hash_address, len(hash_table)):
      if hash_table[index] == 0: # 해당 데이터가 저장된 적 없음
        return None
      elif hash_table[index][0] == index_key:
        return hash_table[index][1]
  else:
    return None
  
save_data('dk', '11111')
save_data('da', '22222')

print(hash_table)
print(read_data('dk'))
print(read_data('da'))