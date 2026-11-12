def solve(n,nums):
    count = 0
    total = 0
    for s in nums:
        if s > 0:
            count += 1
            total += s
    if count == 0:
        return 1, max(nums)
    return count, total