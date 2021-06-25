# 파이썬에서는 해쉬를 별도 구현할 이유가 없음 -> 딕셔너리 타입을 사용하면 됨

# 간단한 해쉬

# hash table 만들기
hash_table = list([0 for i in range(10)])
print(hash_table)

# 초간단 해쉬 함수
# 가장 간단한 방식이 Division 법 (나누기를 통한 나머지 값을 사용하는 기법)
def hash_func(key):
  address = key % 5
  return address

# 해쉬 테이블에 저장
def storage_data(data, value):
  key = ord(data[0])
  hash_address = hash_func(key)
  hash_table[hash_address] = value
  
storage_data('Andy', '01011111111')
storage_data('Dave', '01022222222')
storage_data('Trump', '01033333333')

# 실제 데이터 저장
def get_data(data):
  key = ord(data[0])
  hash_address = hash_func(key)
  return hash_table[hash_address]

print(hash_table)
print(get_data('Andy'))