def quick_sort(lp, rp):
  if lp < rp:
    pivot = arr[rp]
    pos = lp
    for i in range(lp, rp):
      if arr[i] <= pivot:
        arr[i], arr[pos] = arr[pos], arr[i]
        pos += 1
    arr[pos], arr[rp] = arr[rp], arr[pos]
    quick_sort(lp, pos - 1)
    quick_sort(pos + 1, rp)

if __name__ == '__main__':
  arr = [45, 21, 23, 36, 15, 67, 11, 60, 20, 33]
  print('Before sort : ', end =' ')
  print(arr)
  quick_sort(0, 9)
  print('After sort : ', end =' ')
  print(arr)