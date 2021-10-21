def merge_sort(lp, rp):
  if lp < rp:
    mid = (lp + rp) // 2
    merge_sort(lp, mid)
    merge_sort(mid + 1, rp)
    p1 = lp
    p2 = mid + 1
    tmp = []
    while p1 <= mid and p2 <= rp:
      if arr[p1] < arr[p2]:
        tmp.append(arr[p1])
        p1 += 1
      else:
        tmp.append(arr[p2])
        p2 += 1
    if p1 <= mid:
      tmp += arr[p1:mid+1]
    if p2 <= rp:
      tmp += arr[p2:rp+1]
    for i in range(len(tmp)):
      arr[lp + i] = tmp[i]

if __name__ == '__main__':
  arr = [23, 11, 45, 36, 15, 67, 33, 21]
  print('Before sort : ', end =' ')
  print(arr)
  merge_sort(0, 7)
  print('After sort : ', end =' ')
  print(arr)