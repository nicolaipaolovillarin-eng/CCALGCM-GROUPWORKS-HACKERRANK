def solve(n,k):
    # solve problem here. Return correct answer
    l = [1,1]
    
    while len(l) < n:
        if l[-1] < k:
            l.append(l[-2] + l[-1])
        else:
            l.append(k+1)
    
    i = len(l)
    while True:
        if i == 0:
            return "H"
        elif i == 1:
            return "A"
        
        if l[i-2] <= k:
            k -= l[i-2]
            i -= 1
        else:
            i -= 2
        
 
    

n, k = list(map(int,input().rstrip().split(" ")))
print(solve(n,k))
