c, m = [0, 0, 0], [0, 0, 0]

for i in range(3):
  capacity, milk = map(int, input().split())
  c[i] = capacity
  m[i] = milk

for i in range(100):
  idx = i % 3
  next_idx = (i + 1) % 3
  # 따로 나누어 작성할 경우 먼저 작성한 변수의 값이 바뀌기 때문에
  # m[idx] = max(m[idx] - (c[next_idx] - m[next_idx]), 0)
  # m[next_idx] = min(c[next_idx], m[idx] + m[next_idx])
  # 아래와 같이 동시에 값이 변할 수 있도록 작성 한다.
  m[idx], m[next_idx] = max(m[idx] - (c[next_idx] - m[next_idx]), 0), min(c[next_idx], m[idx] + m[next_idx])

for i in m:
  print(i)