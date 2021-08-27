stack = []
operations = int(input().strip())
max_elem = 0

for _ in range(operations):
    query = list(map(int, input().strip().split()))
    
    if query[0] == 1:
        max_elem = max(max_elem, query[1])
        stack.append(query[1])
    if query[0] == 2:
        if stack.pop() == max_elem:
            if len(stack) > 0:
                max_elem = max(stack)
            else:
                max_elem = 0
    if query[0] == 3:
        print(max_elem)