import sys
input = sys.stdin.readline
n, m = map(int, input().split())
pokemons = dict()
for i in range(n):
  name = input().strip()
  pokemons[i+1] = name
  pokemons[name] = i+1
for _ in range(m):
  q = input().strip()
  if q.isdigit():
    print(pokemons[int(q)])
  else:
    print(pokemons[q])