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
                    
step 1: check the array if the conditions meet to x and/or y
step 2: if so, then subtract P to g, continue until g is 0, if it hasn't reach 0 then,
step 2a: what is the min increase in x to meet the condition 
"""
def solve(x,n,g,y,jobs):
    # compute and return answer here
    #check if there is enough payout to reach g
    if sum(jobs[1]) < g:
        return -1
        
    jobs.sort()
    low = 0
    high = n - 1
    
    #gets the lowest index where D <= x
    while low < high:
        mid = (low + high) // 2
        
        if jobs[mid][0] <= x:
            low = mid
        else:
            high = mid - 1
    
    #check if its enough to get the goal (tentative)
    if jobs[mid][0] <= x:
        if sum(jobs[:mid+1][1]):
    
            
    
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
