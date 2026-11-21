def solve(n, t, duties):
    limit = t * 60
    durations = sorted(wait + completion for _, wait, completion in duties)

    total = 0
    completed = 0

    for duration in durations:
        if total + duration > limit:
            break

        total += duration
        completed += 1

    if completed == 0:
        return "I need to find friends."

    return str(completed)


n, t = map(int, input().split())
duties = []

for _ in range(n):
    name = input()
    wait, completion = map(int, input().split())
    duties.append((name, wait, completion))

print(solve(n, t, duties))
