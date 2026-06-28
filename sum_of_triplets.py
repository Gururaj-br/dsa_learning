def triplet_sum(arr, target):
    arr.sort()
    n = len(arr)
    
    for i in range(n-2):
        left = i + 1
        right = n - 1
        
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            
            if current_sum == target:
                print(arr[i], arr[left], arr[right])
                left += 1
                right -= 1
                
            elif current_sum < target:
                left += 1
                
            else:
                right -= 1


arr = [2, 7, 4, 0, 9, 5, 1, 3]
target = 6

triplet_sum(arr, target)