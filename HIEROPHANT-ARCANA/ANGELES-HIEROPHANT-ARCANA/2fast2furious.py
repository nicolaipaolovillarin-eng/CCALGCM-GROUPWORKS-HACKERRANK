F = None

def solve(k, a):
    global F
    MOD = 1000000007
    if F is None: 
        F = [a[0] % MOD]
        for i in range(1, len(a)):
            F.append((2 * F[-1] + a[i] - a[i-1]) % MOD)
    return F[k]

    
    
    
q, n = list(map(int,input().rstrip().split(" ")))
a = [int(input().rstrip()) for i in range(n)]
outs = []
for i in range(q):
    k = int(input().rstrip())
    outs.append(solve(k,a))
print("{}".format("\n".join(list(map(str,outs)))))
