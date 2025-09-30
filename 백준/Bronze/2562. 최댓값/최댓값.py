int_arr = []
for _ in range(9):
    i = int(input())
    int_arr.append(i)
    
print(max(int_arr),int_arr.index(max(int_arr))+1)