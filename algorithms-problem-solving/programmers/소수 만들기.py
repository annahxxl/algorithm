def solution(nums):
    answer = 0
    nums_len = len(nums)
    primes = set()
    
    for i in range(nums_len):
        for j in range(i+1, nums_len):
            for k in range(j+1, nums_len):
                res = nums[i] + nums[j] + nums[k]
                for num in range(2, res):
                    if res % num == 0:
                        break;
                else:
                    primes.add(res)
                    
    answer = len(primes)
    
    return answer