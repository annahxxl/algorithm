sound = list(map(int, input().split()))
asc_check = True
desc_check = True
for i in range(1, len(sound)):
  if sound[i-1] < sound[i]:
    desc_check = False
  if sound[i-1] > sound[i]:
    asc_check = False
if asc_check==True and desc_check==False:
  print('ascending')
elif asc_check==False and desc_check==True:
  print('descending')
else:
  print('mixed')