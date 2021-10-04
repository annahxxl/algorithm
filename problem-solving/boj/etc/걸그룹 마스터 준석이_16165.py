n, m = map(int, input().split())

team_mem, mem_team = {}, {}

for _ in range(n):
  team_name, mem_num = input(), int(input())
  team_mem[team_name] = []
  for _ in range(mem_num):
    name = input()
    team_mem[team_name].append(name)
    mem_team[name] = team_name

for i in range(m):
  quiz, type = input(), int(input())
  if type:
    print(mem_team[quiz])
  else:
    for mem in sorted(team_mem[quiz]):
      print(mem)