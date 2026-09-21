# Enter your code here. Read input from STDIN. Print output to STDOUT
import os

if __name__ == '__main__':
    stack1 = []
    stack2 = []
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    queries = int(input().strip())

    for query in range(queries):
        
        query = tuple(map(int, input().split()))
        
        match query[0] :
            case 1:
                stack1.append(query[1])
            
            case 2:
                
                if len(stack2) == 0:  
                    while len(stack1) != 0:
                        stack2.append(stack1.pop())
                    
                stack2.pop()
                
            case 3:
                if len(stack2) == 0:
                    fptr.write(str(stack1[0]) + '\n')
                
                else:
                    fptr.write(str(stack2[-1]) + '\n')
                
    fptr.close()
