import hashlib
s = input()
# hashlib.sha256(문자열의 바이트 객체).hexdigest(): 해시 결과 문자열
print(hashlib.sha256(s.encode()).hexdigest())