#print("Hello Git!")
from typing import List

def twoSum(nums: List[int], target: int) -> List[int] :
    
    index = 0
    
    while(nums[index] + nums[index + 1] != target):
        index += 1
    
    return [index, index + 1]

#print(twoSum([2, 3, 5, 7, 8, 10],15))