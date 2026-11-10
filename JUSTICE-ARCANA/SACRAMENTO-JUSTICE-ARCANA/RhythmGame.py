import math as m

def solve(n,r,times):
	# compute for and return answer here
    target = m.ceil(n * (r / 100))
    error = sorted([abs(times[x][0] - times[x][1]) for x in range(n) if times[x][1] != -1])

    if len(error) < target:
        return "It's impossible!"
    else: 
        return error[target - 1]
	
def main():
    n, r = list(map(int,input().strip().split(" ")))
    times = [list(map(int,input().strip().split(" "))) for i in range(n)]
    
    print(solve(n,r,times))

if __name__ == "__main__":
    main()
