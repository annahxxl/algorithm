word = input()
alphabet = list(map(chr, range(ord('a'), ord('z')+1)))

for ch in alphabet:
  print(word.find(ch), end=' ')