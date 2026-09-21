# Enter your code here. Read input from STDIN. Print output to STDOUT
q = int(input())

stack1 = []
stack2 = []

for _ in range(q):
    query = input().split()
    type = int(query[0])

    if type == 1:
        stack1.append(int(query[1]))

    elif type == 2:
        if not stack2:
            while stack1:
                stack2.append(stack1.pop())
        stack2.pop()

    elif type == 3:
        if not stack2:
            while stack1:
                stack2.append(stack1.pop())
        print(stack2[-1])
