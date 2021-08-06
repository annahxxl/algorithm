n = int(input())
nums_n = list(map(int, input().split()))
m = int(input())
nums_m = list(map(int, input().split()))
dic = dict()
for num in nums_n:
  dic[num] = True
for num in nums_m:
  if num in dic:
    print(1)
  else:
    print(0) 

'''
- 파이썬에서는 dictionary 자료형을 해시처럼 사용할 수 있다.
- 본 문제는 set 자료형을 이용해 더욱 간단히 풀 수 있다.

* in 연산 시간복잡도
- list, tuple : 하나하나 순회하기 때문에 O(n)만큼의 시간복잡도를 갖는다.
- set, dictionary : 내부적으로 hash를 통해 저장하므로 접근하는 시간은 O(1)이다. 하지만 해쉬의 충돌이 많아 성능이 떨어지는 경우 O(n)이 걸릴 수도 있다.

n = int(input())
array = set(map(int, input().split()))
m = int(input())
x = list(map(int, input().split()))
for i in x:
  if i not in array:
    print(0)
  else:
    print(1)
'''