def two_sum_sorted(nums, target):
    left , right =  0,len(nums)-1

    while left < right:
        sum = nums[left] + nums[right]
        if sum == target:
            return [left+1 , right+1]
        elif sum < target:
            left+=1
        else:
            right-=1

print(two_sum_sorted([3,4,5,6], 7))  # Output : [1,2]
print(two_sum_sorted([2,7,11,15], 9))    # Output : [
print(two_sum_sorted([2,3,4], 6))      # Output : [1,3]
print(two_sum_sorted([-1,0], -1))      # Output : [1,2]