def solve(n,nums):
  	# solve and return answer here
    total = 0
    count = 0
    
    for x in range(n):
        if nums[x] > 0:
            total += nums[x]
            count += 1
    
    if count > 0:
        return count, total
    else:
        return 1, max(nums)

n = int(input())
nums = [int(input()) for i in range(n)]
ans, total = solve(n,nums)

print("{} {}".format(ans,total))
