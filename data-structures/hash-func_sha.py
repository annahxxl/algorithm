# 파이썬의 hash() 함수는 실행할 때마다 값이 달라질 수 있음

# 유명한 해쉬 함수 : SHA (Secure Hash Algorithm)
# -> 어떤 데이터도 고정된 크기의 유일한 고정갑을 린턴해줌, 해쉬 함수로 유용하게 활용 가능

# SHA-1
import hashlib

data = 'test'.encode() # byte로 변환
hash_object = hashlib.sha1()
hash_object.update(data) # hash_object.update(b'test') : byte로 변환해 넣기
hex_dig = hash_object.hexdigest() # 16진수로 추출
print(hex_dig)

# SHA-256
data = 'test'.encode() # byte로 변환
hash_object = hashlib.sha256()
hash_object.update(data) # hash_object.update(b'test') : byte로 변환해 넣기
hex_dig = hash_object.hexdigest() # 16진수로 추출
print(hex_dig)