s = input()
is_bracket = False
res = ''
tmp = ''

for i in s:
  if i == '<':
    res += tmp[::-1] + i
    tmp = ''
    is_bracket = True
  elif i == '>':
    res += i
    is_bracket = False
  elif i == ' ':
    if not is_bracket:
      res += tmp[::-1] + ' '
      tmp = ''
    else:
      res += ' '
  else:
    if is_bracket:
      res += i
    else:
      tmp += i
res += tmp[::-1]

print(res)