arr = [1,1,2,3,3,3,4,5,5,6,7,8,9,0,10,11,11]
new_arr=[]
for i in arr:
    if i not in new_arr:
        new_arr.append(i)
new_arr.sort()
print(new_arr)
print(set(arr))
print(sorted(new_arr)[::-1])
