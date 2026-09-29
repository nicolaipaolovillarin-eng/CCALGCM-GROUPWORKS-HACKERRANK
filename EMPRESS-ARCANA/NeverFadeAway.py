"""
Solves a test case.

Parameters:
x    : int        - V's current skill level
n    : int        - number of jobs available
g    : int        - V's goal income
y    : int        - V's pay threshold for dangerous jobs
jobs : array-like - list of size (n,2) indicating the jobs. Each element is 
                    comprised of two-integers d (the danger level of the job) 
                    and p (the payout of the job)
"""

#searches for the lowest index that has a D > l
def searchIndex(l,n,jobs):
    low = 0
    high = n-1

    #standard binary search for indexes
    while low < high:
        mid = (low + high) // 2
        
        if jobs[mid][0] >= l:
            high = mid
        else:
            low = mid + 1
            
    return low
    

def solve(x,n,g,y,jobs):
    # compute and return answer here
    
    #edge case
    if sum(j[1] for j in jobs) < g:
        return -1
        
    jobs.sort()

    #high and low of the skill level
    low = 1
    high = jobs[-1][0]
    
    #binary search to find the minimum skill required to achieve the goal
    while low < high:
        mid = (low + high) // 2
        
        index = searchIndex(mid,n,jobs)
        
        #calculates the total payout at this skill level
        total = sum(j[1] for j in jobs[:index]) + sum(j[1] for j in jobs[index:] 
            if (j[0] == mid and j[1] >= y) or (j[0] > mid and j[1] >= y**2))
            
        if total < g:
            low = mid + 1
        else:
            high = mid

    #solution - initial skill level
    return low - x
    
            
    
def main():
    t = int(input())

    ans = []
    for tc in range(t):
        input()
        x,n,g,y = list(map(int,input().split(" ")))

        jobs = [list(map(int,input().split(" "))) for i in range(n)]

        ans.append(solve(x,n,g,y,jobs))

    print("\n".join(list(map(str,ans))))

if __name__ == "__main__":
    main()
