def count_rotations_binary(lst):
    
    length = len(lst) - 1
    low = 0
    high = length
    
    if length == 0 or length == -1 or lst[0] < lst[high]:
        return 0
    
    while True:
        
        mid_index = (high + low) // 2
        mid_num = lst[mid_index]
        prev_num = lst[mid_index - 1]
        
        if prev_num > mid_num and mid_index > 0:
            return mid_index
        
        elif lst[high] > mid_num:
            high = mid_index - 1    # answer is on left
        
        elif lst[high] < mid_num:
            low = mid_index + 1     # answer is on right

print(count_rotations_binary([14, 20, 21, 5, 9, 10]))
print(count_rotations_binary([3, 4, 5, 6, 7, 8, 9, 10, 1, 2]))
print(count_rotations_binary([14]))
print(count_rotations_binary([]))
print(count_rotations_binary([3, 5, 7, 10, 25]))
print(count_rotations_binary([3, 8, 15, 90, 134, 653, 1]))


      
    
               