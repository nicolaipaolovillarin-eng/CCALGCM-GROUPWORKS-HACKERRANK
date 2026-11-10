def solve(n,t,problems):
    # compute and return answer here
    count = 0
    index = 0
    time = sorted(problems[x][0] for x in range(n))

    if t < time[0]:
        return "This exam is impossible!"
    else:
        while t >= time[index] and index < len(time):
            if time[index] != -1:
                t -= time[index]
                count += 1 if t >= 0 else 0
            index += 1
        return count


def main():
    n,t = list(map(int,input().strip().split(' ')))
    problems = [tuple(map(int,input().strip().split(" "))) for i in range(n)]
    print(solve(n,t,problems))

if __name__ == "__main__":
    main()
