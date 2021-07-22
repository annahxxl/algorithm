# 분할 정복
n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
white, blue = 0, 0
def divide(x, y, n): # 가로, 세로, 칸 수
  global white, blue # global 키워드로 전역변수 접근
  check = paper[x][y] # 체크할 색
  for i in range(x, x+n):
    if check == -1:
      break
    for j in range(y, y+n):
      if check != paper[i][j]:
        check = -1
        break
  if check == -1:
    n = n//2
    divide(x, y, n) # 왼쪽 위
    divide(x+n, y, n) # 오른쪽 위
    divide(x, y+n, n) # 왼쪽 아래
    divide(x+n, y+n, n) # 오른쪽 아래
  elif check == 0:
    white += 1
  elif check == 1:
    blue += 1
divide(0, 0, n)
print(white)
print(blue)