def read_input(m,n):
    a = []
    for i in range(m):
        row = list(map(int, input().split()))
        row = [0] + row + [0]
        a.append(row)
    return a


m,n,x,y,z = map(int, input().split())
a = read_input(m, n)

l1 = []
l2 = []
l3 = []
for start in range(1,n+1):
    i = 0
    j = start
    while i < m:
        if a[i][j] == 1 and a[i][j+1] == 1:
            i += 1
            j += 1
        elif a[i][j] == -1 and a[i][j-1] == -1:
            i += 1 
            j -= 1
        else:
            break
    if x < i:
        l1 += [start - 1]
    if y < i:
        l2 += [start - 1]
    if z < i:
        l3 += [start - 1]
        
result = [l1, l2, l3]
for row in result:
    if not row:
        row += [-1]
print(result)