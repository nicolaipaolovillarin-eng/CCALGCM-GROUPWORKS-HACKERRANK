import math

"""
Parameters:
s : float - target rate as described in problem
d : float - constant in formula described in problem
k : float - constant in formula described in problem
a : float - constant in formula described in problem

Return:
A STRING containing the answer
"""
def solve(s,d,k,a):
	# compute and return answer here
    low = 0.0
    high = 1.0
    
    while high - low > 1e-6:
        x = (low + high) / 2
        rate = 1 - pow(1 / (1 + math.exp(-k*(x-0.5))),a) + d  

        if rate > s:
            low = x
        else:
            high = x
            
    x = (low + high) / 2
    rate = 1 - pow(1 / (1 + math.exp(-k*(x-0.5))),a) + d
    
    if abs(rate - s) <= 1e-6:
            return str(x)
    else:
        return "Sweet spot cannot be reached! Those cheeky developers!"
  
def main():
    n = int(input().strip())
    vals = [list(map(float,input().strip().split(" "))) \
                    for i in range(n)]
    ans = [solve(s,d,k,a) for s,d,k,a in vals]
    print("\n".join([a for a in ans]))

if __name__ == "__main__":
    main()
