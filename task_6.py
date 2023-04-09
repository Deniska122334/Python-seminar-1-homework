x = list(map(int, list(input())))

left = sum(x[0:-3]) 
right = sum(x[-3:]) 

if left == right:
    print("YES")
else:
    print("NO")
