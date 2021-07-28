n = int(input())
nums = list(map(int, input().split()))
nums2 = list(sorted(set(nums)))
dic = dict()
for i in range(len(nums2)):
  dic[nums2[i]] = i
for i in nums:
  print(dic[i], end=' ')